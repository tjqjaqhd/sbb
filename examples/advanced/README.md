# 고급자 실습 예제

## 📝 목차
1. [Flask 웹 프레임워크](#flask-웹-프레임워크)
2. [데이터베이스 연동](#데이터베이스-연동)
3. [RESTful API 개발](#restful-api-개발)
4. [비동기 프로그래밍](#비동기-프로그래밍)
5. [종합 프로젝트](#종합-프로젝트)

---

## Flask 웹 프레임워크

### 예제 1: 블로그 시스템
```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 데이터베이스 모델
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    tags = db.relationship('Tag', secondary='post_tags', backref='posts')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    posts = db.relationship('Post', backref='category', lazy=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

# 다대다 관계 테이블
post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

# 라우트 정의
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(
        page=page, per_page=5, error_out=False
    )
    categories = Category.query.all()
    return render_template('index.html', posts=posts, categories=categories)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('로그인 성공!', 'success')
            return redirect(url_for('index'))
        else:
            flash('잘못된 사용자명 또는 비밀번호입니다.', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # 중복 확인
        if User.query.filter_by(username=username).first():
            flash('이미 존재하는 사용자명입니다.', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('이미 존재하는 이메일입니다.', 'error')
            return render_template('register.html')
        
        # 새 사용자 생성
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('회원가입이 완료되었습니다.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('로그아웃되었습니다.', 'info')
    return redirect(url_for('index'))

@app.route('/write', methods=['GET', 'POST'])
def write_post():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form.get('category_id')
        tag_names = request.form.get('tags', '').split(',')
        
        # 게시글 생성
        post = Post(
            title=title,
            content=content,
            user_id=session['user_id'],
            category_id=category_id if category_id else None
        )
        
        # 태그 처리
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if tag_name:
                tag = Tag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    db.session.add(tag)
                post.tags.append(tag)
        
        db.session.add(post)
        db.session.commit()
        
        flash('게시글이 작성되었습니다.', 'success')
        return redirect(url_for('view_post', id=post.id))
    
    categories = Category.query.all()
    return render_template('write.html', categories=categories)

@app.route('/post/<int:id>')
def view_post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', post=post)

@app.route('/category/<int:id>')
def view_category(id):
    category = Category.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(category_id=id).order_by(Post.created_at.desc()).paginate(
        page=page, per_page=5, error_out=False
    )
    return render_template('category.html', category=category, posts=posts)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        posts = Post.query.filter(
            db.or_(
                Post.title.contains(query),
                Post.content.contains(query)
            )
        ).order_by(Post.created_at.desc()).all()
    else:
        posts = []
    
    return render_template('search.html', posts=posts, query=query)

# 데이터베이스 초기화
@app.before_first_request
def create_tables():
    db.create_all()
    
    # 기본 카테고리 생성
    if not Category.query.first():
        categories = [
            Category(name='일반', description='일반적인 주제'),
            Category(name='기술', description='기술 관련 내용'),
            Category(name='일상', description='일상 이야기'),
            Category(name='리뷰', description='제품 및 서비스 리뷰')
        ]
        for category in categories:
            db.session.add(category)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML 템플릿 예제

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}파이썬 블로그{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">파이썬 블로그</a>
            <div class="navbar-nav ms-auto">
                {% if session.user_id %}
                    <a class="nav-link" href="{{ url_for('write_post') }}">글쓰기</a>
                    <a class="nav-link" href="{{ url_for('logout') }}">로그아웃 ({{ session.username }})</a>
                {% else %}
                    <a class="nav-link" href="{{ url_for('login') }}">로그인</a>
                    <a class="nav-link" href="{{ url_for('register') }}">회원가입</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ 'danger' if category == 'error' else category }} alert-dismissible fade show">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## 데이터베이스 연동

### 예제 2: SQLAlchemy를 이용한 고급 데이터베이스 작업
```python
# advanced_db.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from datetime import datetime, timedelta
import json

Base = declarative_base()

# 데이터베이스 모델 정의
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    orders = relationship("Order", back_populates="user")
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock_quantity': self.stock_quantity,
            'category': self.category.name if self.category else None
        }

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    products = relationship("Product", back_populates="category")

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String(20), default='pending')  # pending, confirmed, shipped, delivered, cancelled
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
    
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.username,
            'total_amount': self.total_amount,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'items': [item.to_dict() for item in self.order_items]
        }

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)  # 주문 당시 가격
    
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")
    
    def to_dict(self):
        return {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': self.price,
            'subtotal': self.quantity * self.price
        }

class ECommerceDB:
    """전자상거래 데이터베이스 관리 클래스"""
    
    def __init__(self, db_url='sqlite:///ecommerce.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def close(self):
        """데이터베이스 연결 종료"""
        self.session.close()
    
    # 사용자 관련 메서드
    def create_user(self, username, email):
        """사용자 생성"""
        user = User(username=username, email=email)
        self.session.add(user)
        self.session.commit()
        return user
    
    def get_user(self, user_id):
        """사용자 조회"""
        return self.session.query(User).filter(User.id == user_id).first()
    
    def get_user_by_username(self, username):
        """사용자명으로 조회"""
        return self.session.query(User).filter(User.username == username).first()
    
    # 상품 관련 메서드
    def create_product(self, name, description, price, stock_quantity, category_name=None):
        """상품 생성"""
        category = None
        if category_name:
            category = self.session.query(Category).filter(Category.name == category_name).first()
            if not category:
                category = Category(name=category_name)
                self.session.add(category)
                self.session.flush()  # ID 생성을 위해
        
        product = Product(
            name=name,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            category_id=category.id if category else None
        )
        self.session.add(product)
        self.session.commit()
        return product
    
    def search_products(self, keyword=None, category_name=None, min_price=None, max_price=None):
        """상품 검색"""
        query = self.session.query(Product)
        
        if keyword:
            query = query.filter(
                (Product.name.contains(keyword)) |
                (Product.description.contains(keyword))
            )
        
        if category_name:
            query = query.join(Category).filter(Category.name == category_name)
        
        if min_price:
            query = query.filter(Product.price >= min_price)
        
        if max_price:
            query = query.filter(Product.price <= max_price)
        
        return query.all()
    
    def update_stock(self, product_id, new_quantity):
        """재고 업데이트"""
        product = self.session.query(Product).filter(Product.id == product_id).first()
        if product:
            product.stock_quantity = new_quantity
            self.session.commit()
            return True
        return False
    
    # 주문 관련 메서드
    def create_order(self, user_id, items):
        """주문 생성
        items: [{'product_id': 1, 'quantity': 2}, ...]
        """
        total_amount = 0
        order_items = []
        
        # 재고 확인 및 주문 아이템 준비
        for item in items:
            product = self.session.query(Product).filter(Product.id == item['product_id']).first()
            if not product:
                raise ValueError(f"상품 ID {item['product_id']}를 찾을 수 없습니다.")
            
            if product.stock_quantity < item['quantity']:
                raise ValueError(f"재고 부족: {product.name} (재고: {product.stock_quantity})")
            
            subtotal = product.price * item['quantity']
            total_amount += subtotal
            
            order_items.append({
                'product': product,
                'quantity': item['quantity'],
                'price': product.price
            })
        
        # 주문 생성
        order = Order(user_id=user_id, total_amount=total_amount)
        self.session.add(order)
        self.session.flush()  # order.id 생성
        
        # 주문 아이템 생성 및 재고 차감
        for item_data in order_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item_data['product'].id,
                quantity=item_data['quantity'],
                price=item_data['price']
            )
            self.session.add(order_item)
            
            # 재고 차감
            item_data['product'].stock_quantity -= item_data['quantity']
        
        self.session.commit()
        return order
    
    def get_order(self, order_id):
        """주문 조회"""
        return self.session.query(Order).filter(Order.id == order_id).first()
    
    def get_user_orders(self, user_id):
        """사용자 주문 목록"""
        return self.session.query(Order).filter(Order.user_id == user_id).order_by(Order.created_at.desc()).all()
    
    def update_order_status(self, order_id, status):
        """주문 상태 업데이트"""
        order = self.session.query(Order).filter(Order.id == order_id).first()
        if order:
            order.status = status
            self.session.commit()
            return True
        return False
    
    # 통계 및 분석 메서드
    def get_sales_report(self, start_date=None, end_date=None):
        """매출 보고서"""
        query = self.session.query(Order)
        
        if start_date:
            query = query.filter(Order.created_at >= start_date)
        if end_date:
            query = query.filter(Order.created_at <= end_date)
        
        orders = query.all()
        
        total_sales = sum(order.total_amount for order in orders)
        total_orders = len(orders)
        avg_order_value = total_sales / total_orders if total_orders > 0 else 0
        
        return {
            'total_sales': total_sales,
            'total_orders': total_orders,
            'average_order_value': avg_order_value,
            'orders': [order.to_dict() for order in orders]
        }
    
    def get_popular_products(self, limit=10):
        """인기 상품 조회"""
        popular_products = self.session.query(
            Product.id,
            Product.name,
            func.sum(OrderItem.quantity).label('total_sold')
        ).join(OrderItem).group_by(Product.id).order_by(
            func.sum(OrderItem.quantity).desc()
        ).limit(limit).all()
        
        return [
            {
                'product_id': product.id,
                'product_name': product.name,
                'total_sold': product.total_sold
            }
            for product in popular_products
        ]
    
    def get_low_stock_products(self, threshold=10):
        """재고 부족 상품"""
        return self.session.query(Product).filter(Product.stock_quantity <= threshold).all()

# 사용 예제
def ecommerce_demo():
    """전자상거래 데모"""
    db = ECommerceDB()
    
    try:
        # 사용자 생성
        user1 = db.create_user("홍길동", "hong@example.com")
        user2 = db.create_user("김영희", "kim@example.com")
        
        # 상품 생성
        product1 = db.create_product("아이폰 14", "최신 아이폰", 1200000, 50, "전자기기")
        product2 = db.create_product("맥북 프로", "고성능 노트북", 2500000, 20, "전자기기")
        product3 = db.create_product("파이썬 책", "파이썬 학습서", 30000, 100, "도서")
        
        print("상품이 생성되었습니다.")
        
        # 상품 검색
        print("\n=== 상품 검색 (키워드: 아이폰) ===")
        search_results = db.search_products(keyword="아이폰")
        for product in search_results:
            print(f"- {product.name}: {product.price:,}원")
        
        # 주문 생성
        print("\n=== 주문 생성 ===")
        order_items = [
            {'product_id': product1.id, 'quantity': 2},
            {'product_id': product3.id, 'quantity': 1}
        ]
        
        order = db.create_order(user1.id, order_items)
        print(f"주문 생성 완료 - 주문번호: {order.id}, 총액: {order.total_amount:,}원")
        
        # 주문 조회
        print("\n=== 주문 상세 ===")
        order_detail = db.get_order(order.id)
        print(json.dumps(order_detail.to_dict(), ensure_ascii=False, indent=2))
        
        # 매출 보고서
        print("\n=== 매출 보고서 ===")
        sales_report = db.get_sales_report()
        print(f"총 매출: {sales_report['total_sales']:,}원")
        print(f"총 주문 수: {sales_report['total_orders']}건")
        print(f"평균 주문 금액: {sales_report['average_order_value']:,.0f}원")
        
        # 인기 상품
        print("\n=== 인기 상품 ===")
        popular_products = db.get_popular_products(5)
        for product in popular_products:
            print(f"- {product['product_name']}: {product['total_sold']}개 판매")
        
        # 재고 부족 상품
        print("\n=== 재고 부족 상품 (30개 이하) ===")
        low_stock = db.get_low_stock_products(30)
        for product in low_stock:
            print(f"- {product.name}: {product.stock_quantity}개 남음")
    
    except Exception as e:
        print(f"오류 발생: {e}")
    
    finally:
        db.close()

if __name__ == "__main__":
    ecommerce_demo()
```

---

## RESTful API 개발

### 예제 3: Flask-RESTful을 이용한 API 서버
```python
# api_server.py
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields, ValidationError
from datetime import datetime, timedelta
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-jwt-secret-key'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

# 데이터베이스 모델
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Marshmallow 스키마 (직렬화/검증)
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=lambda x: len(x) >= 3)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True, validate=lambda x: len(x) >= 6)
    created_at = fields.DateTime(dump_only=True)

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=lambda x: len(x) >= 1)
    content = fields.Str(required=True, validate=lambda x: len(x) >= 1)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    author_id = fields.Int(dump_only=True)
    author = fields.Nested(UserSchema, only=['id', 'username'], dump_only=True)

# 스키마 인스턴스
user_schema = UserSchema()
users_schema = UserSchema(many=True)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

# API 리소스 클래스
class AuthRegister(Resource):
    def post(self):
        """사용자 등록"""
        try:
            # 요청 데이터 검증
            json_data = request.get_json()
            if not json_data:
                return {'message': 'JSON 데이터가 필요합니다.'}, 400
            
            data = user_schema.load(json_data)
            
            # 중복 확인
            if User.query.filter_by(username=data['username']).first():
                return {'message': '이미 존재하는 사용자명입니다.'}, 400
            
            if User.query.filter_by(email=data['email']).first():
                return {'message': '이미 존재하는 이메일입니다.'}, 400
            
            # 사용자 생성
            user = User(username=data['username'], email=data['email'])
            user.set_password(data['password'])
            db.session.add(user)
            db.session.commit()
            
            return {
                'message': '회원가입이 완료되었습니다.',
                'user': user_schema.dump(user)
            }, 201
            
        except ValidationError as err:
            return {'message': '검증 오류', 'errors': err.messages}, 400
        except Exception as e:
            return {'message': '서버 오류가 발생했습니다.'}, 500

class AuthLogin(Resource):
    def post(self):
        """로그인"""
        try:
            json_data = request.get_json()
            username = json_data.get('username')
            password = json_data.get('password')
            
            if not username or not password:
                return {'message': '사용자명과 비밀번호가 필요합니다.'}, 400
            
            user = User.query.filter_by(username=username).first()
            
            if user and user.check_password(password):
                access_token = create_access_token(identity=user.id)
                return {
                    'message': '로그인 성공',
                    'access_token': access_token,
                    'user': user_schema.dump(user)
                }, 200
            else:
                return {'message': '잘못된 사용자명 또는 비밀번호입니다.'}, 401
                
        except Exception as e:
            return {'message': '서버 오류가 발생했습니다.'}, 500

class UserList(Resource):
    def get(self):
        """사용자 목록 조회"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        users = User.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return {
            'users': users_schema.dump(users.items),
            'pagination': {
                'page': page,
                'pages': users.pages,
                'per_page': per_page,
                'total': users.total
            }
        }, 200

class UserDetail(Resource):
    def get(self, user_id):
        """사용자 상세 조회"""
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user), 200

class PostList(Resource):
    @jwt_required()
    def post(self):
        """게시글 작성"""
        try:
            current_user_id = get_jwt_identity()
            json_data = request.get_json()
            
            if not json_data:
                return {'message': 'JSON 데이터가 필요합니다.'}, 400
            
            data = post_schema.load(json_data)
            
            post = Post(
                title=data['title'],
                content=data['content'],
                author_id=current_user_id
            )
            db.session.add(post)
            db.session.commit()
            
            return {
                'message': '게시글이 작성되었습니다.',
                'post': post_schema.dump(post)
            }, 201
            
        except ValidationError as err:
            return {'message': '검증 오류', 'errors': err.messages}, 400
        except Exception as e:
            return {'message': '서버 오류가 발생했습니다.'}, 500
    
    def get(self):
        """게시글 목록 조회"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search = request.args.get('search', '')
        
        query = Post.query
        
        if search:
            query = query.filter(
                db.or_(
                    Post.title.contains(search),
                    Post.content.contains(search)
                )
            )
        
        posts = query.order_by(Post.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return {
            'posts': posts_schema.dump(posts.items),
            'pagination': {
                'page': page,
                'pages': posts.pages,
                'per_page': per_page,
                'total': posts.total
            }
        }, 200

class PostDetail(Resource):
    def get(self, post_id):
        """게시글 상세 조회"""
        post = Post.query.get_or_404(post_id)
        return post_schema.dump(post), 200
    
    @jwt_required()
    def put(self, post_id):
        """게시글 수정"""
        try:
            current_user_id = get_jwt_identity()
            post = Post.query.get_or_404(post_id)
            
            if post.author_id != current_user_id:
                return {'message': '권한이 없습니다.'}, 403
            
            json_data = request.get_json()
            if not json_data:
                return {'message': 'JSON 데이터가 필요합니다.'}, 400
            
            data = post_schema.load(json_data, partial=True)
            
            if 'title' in data:
                post.title = data['title']
            if 'content' in data:
                post.content = data['content']
            
            post.updated_at = datetime.utcnow()
            db.session.commit()
            
            return {
                'message': '게시글이 수정되었습니다.',
                'post': post_schema.dump(post)
            }, 200
            
        except ValidationError as err:
            return {'message': '검증 오류', 'errors': err.messages}, 400
        except Exception as e:
            return {'message': '서버 오류가 발생했습니다.'}, 500
    
    @jwt_required()
    def delete(self, post_id):
        """게시글 삭제"""
        try:
            current_user_id = get_jwt_identity()
            post = Post.query.get_or_404(post_id)
            
            if post.author_id != current_user_id:
                return {'message': '권한이 없습니다.'}, 403
            
            db.session.delete(post)
            db.session.commit()
            
            return {'message': '게시글이 삭제되었습니다.'}, 200
            
        except Exception as e:
            return {'message': '서버 오류가 발생했습니다.'}, 500

# API 엔드포인트 등록
api.add_resource(AuthRegister, '/api/auth/register')
api.add_resource(AuthLogin, '/api/auth/login')
api.add_resource(UserList, '/api/users')
api.add_resource(UserDetail, '/api/users/<int:user_id>')
api.add_resource(PostList, '/api/posts')
api.add_resource(PostDetail, '/api/posts/<int:post_id>')

# 에러 핸들러
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': '리소스를 찾을 수 없습니다.'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': '서버 내부 오류가 발생했습니다.'}), 500

# JWT 에러 핸들러
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({'message': '토큰이 만료되었습니다.'}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'message': '유효하지 않은 토큰입니다.'}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({'message': '인증 토큰이 필요합니다.'}), 401

# 데이터베이스 초기화
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

### API 테스트 클라이언트 예제
```python
# api_client.py
import requests
import json

class APIClient:
    """API 클라이언트"""
    
    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url
        self.session = requests.Session()
        self.access_token = None
    
    def register(self, username, email, password):
        """회원가입"""
        url = f"{self.base_url}/api/auth/register"
        data = {
            'username': username,
            'email': email,
            'password': password
        }
        response = self.session.post(url, json=data)
        return response.json(), response.status_code
    
    def login(self, username, password):
        """로그인"""
        url = f"{self.base_url}/api/auth/login"
        data = {
            'username': username,
            'password': password
        }
        response = self.session.post(url, json=data)
        
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get('access_token')
            self.session.headers.update({
                'Authorization': f'Bearer {self.access_token}'
            })
        
        return response.json(), response.status_code
    
    def get_posts(self, page=1, per_page=10, search=''):
        """게시글 목록 조회"""
        url = f"{self.base_url}/api/posts"
        params = {
            'page': page,
            'per_page': per_page,
            'search': search
        }
        response = self.session.get(url, params=params)
        return response.json(), response.status_code
    
    def create_post(self, title, content):
        """게시글 작성"""
        url = f"{self.base_url}/api/posts"
        data = {
            'title': title,
            'content': content
        }
        response = self.session.post(url, json=data)
        return response.json(), response.status_code
    
    def get_post(self, post_id):
        """게시글 상세 조회"""
        url = f"{self.base_url}/api/posts/{post_id}"
        response = self.session.get(url)
        return response.json(), response.status_code
    
    def update_post(self, post_id, title=None, content=None):
        """게시글 수정"""
        url = f"{self.base_url}/api/posts/{post_id}"
        data = {}
        if title:
            data['title'] = title
        if content:
            data['content'] = content
        
        response = self.session.put(url, json=data)
        return response.json(), response.status_code
    
    def delete_post(self, post_id):
        """게시글 삭제"""
        url = f"{self.base_url}/api/posts/{post_id}"
        response = self.session.delete(url)
        return response.json(), response.status_code

# 테스트 예제
def test_api():
    """API 테스트"""
    client = APIClient()
    
    print("=== API 테스트 시작 ===")
    
    # 회원가입
    print("\n1. 회원가입")
    result, status = client.register("testuser", "test@example.com", "password123")
    print(f"Status: {status}")
    print(f"Response: {json.dumps(result, ensure_ascii=False, indent=2)}")
    
    # 로그인
    print("\n2. 로그인")
    result, status = client.login("testuser", "password123")
    print(f"Status: {status}")
    print(f"Response: {json.dumps(result, ensure_ascii=False, indent=2)}")
    
    # 게시글 작성
    print("\n3. 게시글 작성")
    result, status = client.create_post("첫 번째 게시글", "파이썬 API 테스트 내용입니다.")
    print(f"Status: {status}")
    print(f"Response: {json.dumps(result, ensure_ascii=False, indent=2)}")
    
    if status == 201:
        post_id = result['post']['id']
        
        # 게시글 조회
        print("\n4. 게시글 상세 조회")
        result, status = client.get_post(post_id)
        print(f"Status: {status}")
        print(f"Response: {json.dumps(result, ensure_ascii=False, indent=2)}")
        
        # 게시글 수정
        print("\n5. 게시글 수정")
        result, status = client.update_post(post_id, title="수정된 제목")
        print(f"Status: {status}")
        print(f"Response: {json.dumps(result, ensure_ascii=False, indent=2)}")
    
    # 게시글 목록 조회
    print("\n6. 게시글 목록 조회")
    result, status = client.get_posts()
    print(f"Status: {status}")
    print(f"Response: {json.dumps(result, ensure_ascii=False, indent=2)}")

if __name__ == "__main__":
    test_api()
```

---

## 종합 프로젝트

### 프로젝트: 전자상거래 플랫폼 MVP
고급 단계에서 학습한 모든 기술을 종합하여 본격적인 전자상거래 플랫폼을 구축해보세요.

**기능 요구사항:**

**사용자 기능:**
- 회원가입/로그인/로그아웃
- 상품 검색 및 필터링
- 장바구니 관리
- 주문 및 결제
- 주문 내역 조회
- 리뷰 작성

**관리자 기능:**
- 상품 관리 (CRUD)
- 주문 관리
- 사용자 관리
- 매출 통계 및 분석
- 재고 관리

**기술 스택:**
- **Backend**: Flask + SQLAlchemy
- **Database**: PostgreSQL (또는 MySQL)
- **API**: RESTful API with JWT 인증
- **Frontend**: React (또는 Vue.js)
- **Cache**: Redis
- **Queue**: Celery (비동기 작업)
- **Deployment**: Docker + Docker Compose
- **CI/CD**: GitHub Actions

**구현 단계:**
1. 데이터베이스 설계 및 모델 구현
2. 인증 시스템 구축
3. 상품 관리 API 개발
4. 주문 시스템 구현
5. 프론트엔드 연동
6. 성능 최적화 (캐싱, 인덱싱)
7. 테스트 코드 작성
8. 배포 환경 구축

이 프로젝트를 통해 실무에서 요구되는 모든 기술을 경험하고, 포트폴리오로 활용할 수 있는 완성도 높은 애플리케이션을 개발할 수 있습니다.

---

*고급 과정을 완주하셨다면 이제 전문적인 파이썬 개발자로서의 역량을 갖추었습니다. 지속적인 학습과 실전 경험을 통해 더욱 발전시켜 나가세요!*