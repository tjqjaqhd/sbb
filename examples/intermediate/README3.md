# 중급자 실습 예제

## 📝 목차
1. [객체지향 프로그래밍](#객체지향-프로그래밍)
2. [파일 처리 및 예외 처리](#파일-처리-및-예외-처리)
3. [라이브러리 활용](#라이브러리-활용)
4. [종합 프로젝트](#종합-프로젝트)

---

## 객체지향 프로그래밍

### 예제 1: 은행 계좌 관리 시스템
```python
# bank_account.py
from datetime import datetime

class BankAccount:
    """은행 계좌 클래스"""
    
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
        self.created_date = datetime.now()
    
    def deposit(self, amount):
        """입금"""
        if amount <= 0:
            raise ValueError("입금 금액은 0보다 커야 합니다.")
        
        self.balance += amount
        transaction = {
            'type': '입금',
            'amount': amount,
            'balance': self.balance,
            'date': datetime.now()
        }
        self.transaction_history.append(transaction)
        return True
    
    def withdraw(self, amount):
        """출금"""
        if amount <= 0:
            raise ValueError("출금 금액은 0보다 커야 합니다.")
        
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다.")
        
        self.balance -= amount
        transaction = {
            'type': '출금',
            'amount': amount,
            'balance': self.balance,
            'date': datetime.now()
        }
        self.transaction_history.append(transaction)
        return True
    
    def transfer(self, target_account, amount):
        """계좌 이체"""
        if amount <= 0:
            raise ValueError("이체 금액은 0보다 커야 합니다.")
        
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다.")
        
        # 출금
        self.balance -= amount
        transaction = {
            'type': '이체(출금)',
            'amount': amount,
            'target': target_account.account_number,
            'balance': self.balance,
            'date': datetime.now()
        }
        self.transaction_history.append(transaction)
        
        # 상대방 계좌에 입금
        target_account.balance += amount
        target_transaction = {
            'type': '이체(입금)',
            'amount': amount,
            'from': self.account_number,
            'balance': target_account.balance,
            'date': datetime.now()
        }
        target_account.transaction_history.append(target_transaction)
        
        return True
    
    def get_balance(self):
        """잔액 조회"""
        return self.balance
    
    def get_transaction_history(self, limit=None):
        """거래 내역 조회"""
        history = self.transaction_history
        if limit:
            history = history[-limit:]
        return history
    
    def __str__(self):
        return f"계좌번호: {self.account_number}, 예금주: {self.account_holder}, 잔액: {self.balance:,}원"

class SavingsAccount(BankAccount):
    """적금 계좌 클래스"""
    
    def __init__(self, account_holder, account_number, initial_balance=0, interest_rate=0.02):
        super().__init__(account_holder, account_number, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """이자 추가"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        transaction = {
            'type': '이자',
            'amount': interest,
            'balance': self.balance,
            'date': datetime.now()
        }
        self.transaction_history.append(transaction)
        return interest

# 사용 예제
def bank_system_demo():
    print("=== 은행 계좌 관리 시스템 ===")
    
    # 계좌 생성
    account1 = BankAccount("김파이썬", "123-456-789", 100000)
    account2 = BankAccount("이자바", "987-654-321", 50000)
    savings = SavingsAccount("박적금", "111-222-333", 1000000, 0.03)
    
    try:
        # 입금
        account1.deposit(50000)
        print(f"입금 후: {account1}")
        
        # 출금
        account1.withdraw(30000)
        print(f"출금 후: {account1}")
        
        # 이체
        account1.transfer(account2, 20000)
        print(f"이체 후 - 보내는 계좌: {account1}")
        print(f"이체 후 - 받는 계좌: {account2}")
        
        # 이자 추가 (적금 계좌)
        interest = savings.add_interest()
        print(f"이자 {interest:,.0f}원 추가 후: {savings}")
        
        # 거래 내역
        print("\n=== 거래 내역 ===")
        for transaction in account1.get_transaction_history():
            print(f"{transaction['date'].strftime('%Y-%m-%d %H:%M')} - "
                  f"{transaction['type']}: {transaction['amount']:,}원 "
                  f"(잔액: {transaction['balance']:,}원)")
    
    except ValueError as e:
        print(f"오류: {e}")

if __name__ == "__main__":
    bank_system_demo()
```

### 예제 2: 도서관 관리 시스템
```python
# library_system.py
from datetime import datetime, timedelta

class Book:
    """도서 클래스"""
    
    def __init__(self, isbn, title, author, publisher, publication_date):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.is_available = True
        self.borrower = None
        self.borrowed_date = None
        self.due_date = None
    
    def __str__(self):
        status = "대출 가능" if self.is_available else f"대출 중 ({self.borrower})"
        return f"{self.title} - {self.author} [{status}]"

class Member:
    """회원 클래스"""
    
    def __init__(self, member_id, name, phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.borrowed_books = []
        self.join_date = datetime.now()
    
    def can_borrow(self):
        """대출 가능 여부 확인 (최대 3권)"""
        return len(self.borrowed_books) < 3
    
    def __str__(self):
        return f"회원 {self.member_id}: {self.name} (대출중: {len(self.borrowed_books)}권)"

class Library:
    """도서관 클래스"""
    
    def __init__(self, name):
        self.name = name
        self.books = {}  # ISBN을 키로 하는 딕셔너리
        self.members = {}  # member_id를 키로 하는 딕셔너리
        self.loan_period = 14  # 대출 기간 (일)
    
    def add_book(self, book):
        """도서 추가"""
        self.books[book.isbn] = book
        print(f"도서가 추가되었습니다: {book.title}")
    
    def add_member(self, member):
        """회원 추가"""
        self.members[member.member_id] = member
        print(f"회원이 등록되었습니다: {member.name}")
    
    def search_book(self, keyword):
        """도서 검색 (제목 또는 저자)"""
        results = []
        for book in self.books.values():
            if (keyword.lower() in book.title.lower() or 
                keyword.lower() in book.author.lower()):
                results.append(book)
        return results
    
    def borrow_book(self, member_id, isbn):
        """도서 대출"""
        if member_id not in self.members:
            raise ValueError("등록되지 않은 회원입니다.")
        
        if isbn not in self.books:
            raise ValueError("존재하지 않는 도서입니다.")
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        if not member.can_borrow():
            raise ValueError("대출 가능한 권수를 초과했습니다. (최대 3권)")
        
        if not book.is_available:
            raise ValueError("이미 대출 중인 도서입니다.")
        
        # 대출 처리
        book.is_available = False
        book.borrower = member.name
        book.borrowed_date = datetime.now()
        book.due_date = datetime.now() + timedelta(days=self.loan_period)
        
        member.borrowed_books.append(isbn)
        
        print(f"대출 완료: {book.title} (반납 예정일: {book.due_date.strftime('%Y-%m-%d')})")
    
    def return_book(self, member_id, isbn):
        """도서 반납"""
        if member_id not in self.members:
            raise ValueError("등록되지 않은 회원입니다.")
        
        if isbn not in self.books:
            raise ValueError("존재하지 않는 도서입니다.")
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        if book.is_available or isbn not in member.borrowed_books:
            raise ValueError("대출하지 않은 도서입니다.")
        
        # 연체료 계산
        overdue_fee = 0
        if datetime.now() > book.due_date:
            overdue_days = (datetime.now() - book.due_date).days
            overdue_fee = overdue_days * 100  # 하루당 100원
        
        # 반납 처리
        book.is_available = True
        book.borrower = None
        book.borrowed_date = None
        book.due_date = None
        
        member.borrowed_books.remove(isbn)
        
        if overdue_fee > 0:
            print(f"반납 완료: {book.title} (연체료: {overdue_fee}원)")
        else:
            print(f"반납 완료: {book.title}")
    
    def get_overdue_books(self):
        """연체 도서 목록"""
        overdue_books = []
        for book in self.books.values():
            if not book.is_available and datetime.now() > book.due_date:
                overdue_books.append(book)
        return overdue_books
    
    def get_member_books(self, member_id):
        """회원 대출 도서 목록"""
        if member_id not in self.members:
            return []
        
        member = self.members[member_id]
        borrowed_books = []
        for isbn in member.borrowed_books:
            book = self.books[isbn]
            borrowed_books.append(book)
        return borrowed_books

# 사용 예제
def library_demo():
    print("=== 도서관 관리 시스템 ===")
    
    # 도서관 생성
    library = Library("중앙도서관")
    
    # 도서 추가
    books = [
        Book("978-1234567890", "파이썬 프로그래밍", "김파이썬", "코딩출판사", "2023-01-01"),
        Book("978-0987654321", "자료구조와 알고리즘", "이알고", "구조출판사", "2023-02-01"),
        Book("978-1122334455", "웹 개발 입문", "박웹디", "웹출판사", "2023-03-01")
    ]
    
    for book in books:
        library.add_book(book)
    
    # 회원 등록
    members = [
        Member("M001", "홍길동", "010-1234-5678"),
        Member("M002", "김영희", "010-9876-5432")
    ]
    
    for member in members:
        library.add_member(member)
    
    try:
        # 도서 검색
        print("\n=== 도서 검색 (키워드: 파이썬) ===")
        search_results = library.search_book("파이썬")
        for book in search_results:
            print(book)
        
        # 도서 대출
        print("\n=== 도서 대출 ===")
        library.borrow_book("M001", "978-1234567890")
        library.borrow_book("M002", "978-0987654321")
        
        # 대출 목록 확인
        print("\n=== 홍길동 대출 목록 ===")
        borrowed = library.get_member_books("M001")
        for book in borrowed:
            print(f"- {book.title} (반납 예정: {book.due_date.strftime('%Y-%m-%d')})")
        
        # 도서 반납
        print("\n=== 도서 반납 ===")
        library.return_book("M001", "978-1234567890")
        
    except ValueError as e:
        print(f"오류: {e}")

if __name__ == "__main__":
    library_demo()
```

---

## 파일 처리 및 예외 처리

### 예제 3: CSV 파일을 이용한 주소록 관리
```python
# address_book.py
import csv
import os
from datetime import datetime

class Contact:
    """연락처 클래스"""
    
    def __init__(self, name, phone, email, address="", memo=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.memo = memo
        self.created_date = datetime.now()
    
    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'memo': self.memo,
            'created_date': self.created_date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 객체 생성"""
        contact = cls(
            data['name'],
            data['phone'],
            data['email'],
            data.get('address', ''),
            data.get('memo', '')
        )
        if 'created_date' in data:
            contact.created_date = datetime.fromisoformat(data['created_date'])
        return contact
    
    def __str__(self):
        return f"{self.name} ({self.phone}) - {self.email}"

class AddressBook:
    """주소록 클래스"""
    
    def __init__(self, filename="contacts.csv"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()
    
    def add_contact(self, contact):
        """연락처 추가"""
        # 중복 검사
        for existing_contact in self.contacts:
            if existing_contact.phone == contact.phone:
                raise ValueError("이미 등록된 전화번호입니다.")
        
        self.contacts.append(contact)
        self.save_contacts()
        print(f"연락처가 추가되었습니다: {contact.name}")
    
    def search_contact(self, keyword):
        """연락처 검색"""
        results = []
        keyword = keyword.lower()
        
        for contact in self.contacts:
            if (keyword in contact.name.lower() or
                keyword in contact.phone or
                keyword in contact.email.lower()):
                results.append(contact)
        
        return results
    
    def update_contact(self, phone, **kwargs):
        """연락처 수정"""
        for contact in self.contacts:
            if contact.phone == phone:
                for key, value in kwargs.items():
                    if hasattr(contact, key):
                        setattr(contact, key, value)
                self.save_contacts()
                print(f"연락처가 수정되었습니다: {contact.name}")
                return True
        
        raise ValueError("연락처를 찾을 수 없습니다.")
    
    def delete_contact(self, phone):
        """연락처 삭제"""
        for i, contact in enumerate(self.contacts):
            if contact.phone == phone:
                deleted_contact = self.contacts.pop(i)
                self.save_contacts()
                print(f"연락처가 삭제되었습니다: {deleted_contact.name}")
                return True
        
        raise ValueError("연락처를 찾을 수 없습니다.")
    
    def save_contacts(self):
        """CSV 파일로 저장"""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                if self.contacts:
                    fieldnames = ['name', 'phone', 'email', 'address', 'memo', 'created_date']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    
                    for contact in self.contacts:
                        writer.writerow(contact.to_dict())
            
            print(f"주소록이 {self.filename}에 저장되었습니다.")
        
        except IOError as e:
            print(f"파일 저장 중 오류가 발생했습니다: {e}")
    
    def load_contacts(self):
        """CSV 파일에서 불러오기"""
        if not os.path.exists(self.filename):
            print(f"{self.filename} 파일이 없습니다. 새로운 주소록을 시작합니다.")
            return
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.contacts = []
                
                for row in reader:
                    contact = Contact.from_dict(row)
                    self.contacts.append(contact)
            
            print(f"{len(self.contacts)}개의 연락처를 불러왔습니다.")
        
        except IOError as e:
            print(f"파일 읽기 중 오류가 발생했습니다: {e}")
        except csv.Error as e:
            print(f"CSV 파일 형식 오류: {e}")
    
    def list_contacts(self):
        """연락처 목록 출력"""
        if not self.contacts:
            print("등록된 연락처가 없습니다.")
            return
        
        print(f"\n=== 주소록 ({len(self.contacts)}개) ===")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact}")
    
    def get_statistics(self):
        """통계 정보"""
        total = len(self.contacts)
        domains = {}
        
        for contact in self.contacts:
            if '@' in contact.email:
                domain = contact.email.split('@')[1]
                domains[domain] = domains.get(domain, 0) + 1
        
        print(f"\n=== 주소록 통계 ===")
        print(f"총 연락처 수: {total}")
        print(f"가장 많은 이메일 도메인:")
        
        for domain, count in sorted(domains.items(), key=lambda x: x[1], reverse=True)[:3]:
            print(f"  {domain}: {count}개")

def address_book_demo():
    """주소록 데모"""
    print("=== 주소록 관리 프로그램 ===")
    
    address_book = AddressBook()
    
    while True:
        print("\n1. 연락처 추가")
        print("2. 연락처 검색")
        print("3. 연락처 목록")
        print("4. 연락처 수정")
        print("5. 연락처 삭제")
        print("6. 통계 보기")
        print("7. 종료")
        
        choice = input("선택하세요: ").strip()
        
        try:
            if choice == '1':
                name = input("이름: ").strip()
                phone = input("전화번호: ").strip()
                email = input("이메일: ").strip()
                address = input("주소 (선택사항): ").strip()
                memo = input("메모 (선택사항): ").strip()
                
                if not all([name, phone, email]):
                    print("이름, 전화번호, 이메일은 필수 입력 항목입니다.")
                    continue
                
                contact = Contact(name, phone, email, address, memo)
                address_book.add_contact(contact)
            
            elif choice == '2':
                keyword = input("검색 키워드 (이름, 전화번호, 이메일): ").strip()
                results = address_book.search_contact(keyword)
                
                if results:
                    print(f"\n검색 결과 ({len(results)}개):")
                    for i, contact in enumerate(results, 1):
                        print(f"{i}. {contact}")
                else:
                    print("검색 결과가 없습니다.")
            
            elif choice == '3':
                address_book.list_contacts()
            
            elif choice == '4':
                phone = input("수정할 연락처의 전화번호: ").strip()
                print("수정할 정보를 입력하세요 (변경하지 않으려면 엔터):")
                
                updates = {}
                new_name = input("새 이름: ").strip()
                if new_name:
                    updates['name'] = new_name
                
                new_email = input("새 이메일: ").strip()
                if new_email:
                    updates['email'] = new_email
                
                new_address = input("새 주소: ").strip()
                if new_address:
                    updates['address'] = new_address
                
                new_memo = input("새 메모: ").strip()
                if new_memo:
                    updates['memo'] = new_memo
                
                if updates:
                    address_book.update_contact(phone, **updates)
                else:
                    print("수정할 정보가 없습니다.")
            
            elif choice == '5':
                phone = input("삭제할 연락처의 전화번호: ").strip()
                confirm = input(f"정말 삭제하시겠습니까? (y/n): ").strip().lower()
                
                if confirm == 'y':
                    address_book.delete_contact(phone)
                else:
                    print("삭제가 취소되었습니다.")
            
            elif choice == '6':
                address_book.get_statistics()
            
            elif choice == '7':
                print("프로그램을 종료합니다.")
                break
            
            else:
                print("잘못된 선택입니다.")
        
        except ValueError as e:
            print(f"오류: {e}")
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    address_book_demo()
```

---

## 라이브러리 활용

### 예제 4: 웹 API를 이용한 날씨 정보 조회
```python
# weather_app.py
import requests
import json
from datetime import datetime

class WeatherAPI:
    """날씨 API 클래스"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def get_current_weather(self, city):
        """현재 날씨 조회"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'kr'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # HTTP 오류 시 예외 발생
            
            data = response.json()
            return self._parse_current_weather(data)
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"API 요청 중 오류 발생: {e}")
        except json.JSONDecodeError:
            raise Exception("API 응답 형식 오류")
        except KeyError as e:
            raise Exception(f"API 응답 데이터 오류: {e}")
    
    def get_forecast(self, city, days=5):
        """일기예보 조회"""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'kr'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return self._parse_forecast(data, days)
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"API 요청 중 오류 발생: {e}")
        except json.JSONDecodeError:
            raise Exception("API 응답 형식 오류")
        except KeyError as e:
            raise Exception(f"API 응답 데이터 오류: {e}")
    
    def _parse_current_weather(self, data):
        """현재 날씨 데이터 파싱"""
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'visibility': data.get('visibility', 0) / 1000,  # km 변환
            'sunrise': datetime.fromtimestamp(data['sys']['sunrise']),
            'sunset': datetime.fromtimestamp(data['sys']['sunset'])
        }
    
    def _parse_forecast(self, data, days):
        """일기예보 데이터 파싱"""
        forecasts = []
        
        # 3시간 간격 데이터에서 일별 데이터 추출
        daily_data = {}
        
        for item in data['list'][:days * 8]:  # 5일 * 8 (3시간 간격)
            date = datetime.fromtimestamp(item['dt']).date()
            
            if date not in daily_data:
                daily_data[date] = {
                    'temperatures': [],
                    'descriptions': [],
                    'humidity': [],
                    'wind_speed': []
                }
            
            daily_data[date]['temperatures'].append(item['main']['temp'])
            daily_data[date]['descriptions'].append(item['weather'][0]['description'])
            daily_data[date]['humidity'].append(item['main']['humidity'])
            daily_data[date]['wind_speed'].append(item['wind']['speed'])
        
        # 일별 평균/대표값 계산
        for date, day_data in daily_data.items():
            forecast = {
                'date': date,
                'min_temp': round(min(day_data['temperatures'])),
                'max_temp': round(max(day_data['temperatures'])),
                'avg_temp': round(sum(day_data['temperatures']) / len(day_data['temperatures'])),
                'description': max(set(day_data['descriptions']), key=day_data['descriptions'].count),
                'avg_humidity': round(sum(day_data['humidity']) / len(day_data['humidity'])),
                'avg_wind_speed': round(sum(day_data['wind_speed']) / len(day_data['wind_speed']), 1)
            }
            forecasts.append(forecast)
        
        return forecasts

class WeatherApp:
    """날씨 앱 클래스"""
    
    def __init__(self, api_key):
        self.weather_api = WeatherAPI(api_key)
        self.favorite_cities = self._load_favorites()
    
    def _load_favorites(self):
        """즐겨찾는 도시 목록 불러오기"""
        try:
            with open('favorite_cities.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("즐겨찾기 파일 형식 오류")
            return []
    
    def _save_favorites(self):
        """즐겨찾는 도시 목록 저장"""
        try:
            with open('favorite_cities.json', 'w', encoding='utf-8') as file:
                json.dump(self.favorite_cities, file, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"즐겨찾기 저장 오류: {e}")
    
    def add_favorite_city(self, city):
        """즐겨찾는 도시 추가"""
        if city not in self.favorite_cities:
            self.favorite_cities.append(city)
            self._save_favorites()
            print(f"{city}가 즐겨찾기에 추가되었습니다.")
        else:
            print(f"{city}는 이미 즐겨찾기에 있습니다.")
    
    def remove_favorite_city(self, city):
        """즐겨찾는 도시 제거"""
        if city in self.favorite_cities:
            self.favorite_cities.remove(city)
            self._save_favorites()
            print(f"{city}가 즐겨찾기에서 제거되었습니다.")
        else:
            print(f"{city}는 즐겨찾기에 없습니다.")
    
    def show_current_weather(self, city):
        """현재 날씨 표시"""
        try:
            weather = self.weather_api.get_current_weather(city)
            
            print(f"\n=== {weather['city']}, {weather['country']} 현재 날씨 ===")
            print(f"온도: {weather['temperature']}°C (체감온도: {weather['feels_like']}°C)")
            print(f"날씨: {weather['description']}")
            print(f"습도: {weather['humidity']}%")
            print(f"기압: {weather['pressure']} hPa")
            print(f"풍속: {weather['wind_speed']} m/s")
            print(f"가시거리: {weather['visibility']} km")
            print(f"일출: {weather['sunrise'].strftime('%H:%M')}")
            print(f"일몰: {weather['sunset'].strftime('%H:%M')}")
        
        except Exception as e:
            print(f"날씨 정보를 가져오는 중 오류 발생: {e}")
    
    def show_forecast(self, city, days=5):
        """일기예보 표시"""
        try:
            forecasts = self.weather_api.get_forecast(city, days)
            
            print(f"\n=== {city} {days}일 일기예보 ===")
            for forecast in forecasts:
                print(f"{forecast['date'].strftime('%m/%d')}: "
                      f"{forecast['min_temp']}°C ~ {forecast['max_temp']}°C, "
                      f"{forecast['description']}, "
                      f"습도 {forecast['avg_humidity']}%")
        
        except Exception as e:
            print(f"일기예보를 가져오는 중 오류 발생: {e}")
    
    def show_favorite_weather(self):
        """즐겨찾는 도시들의 날씨 요약"""
        if not self.favorite_cities:
            print("즐겨찾는 도시가 없습니다.")
            return
        
        print("\n=== 즐겨찾는 도시 날씨 요약 ===")
        for city in self.favorite_cities:
            try:
                weather = self.weather_api.get_current_weather(city)
                print(f"{weather['city']}: {weather['temperature']}°C, {weather['description']}")
            except Exception as e:
                print(f"{city}: 정보를 가져올 수 없음 ({e})")

def weather_app_demo():
    """날씨 앱 데모"""
    # 실제 사용 시에는 OpenWeatherMap에서 API 키를 발급받아야 합니다
    API_KEY = "your_api_key_here"  # 실제 API 키로 변경 필요
    
    if API_KEY == "your_api_key_here":
        print("API 키를 설정해주세요.")
        print("1. https://openweathermap.org/api에서 무료 API 키 발급")
        print("2. 코드에서 API_KEY 변수 값 변경")
        return
    
    app = WeatherApp(API_KEY)
    
    while True:
        print("\n=== 날씨 정보 앱 ===")
        print("1. 현재 날씨 조회")
        print("2. 일기예보 조회")
        print("3. 즐겨찾기 도시 날씨")
        print("4. 즐겨찾기 추가")
        print("5. 즐겨찾기 제거")
        print("6. 즐겨찾기 목록")
        print("7. 종료")
        
        choice = input("선택하세요: ").strip()
        
        try:
            if choice == '1':
                city = input("도시명을 입력하세요 (영문): ").strip()
                if city:
                    app.show_current_weather(city)
            
            elif choice == '2':
                city = input("도시명을 입력하세요 (영문): ").strip()
                days = input("예보 일수 (1-5, 기본값 5): ").strip()
                
                if city:
                    try:
                        days = int(days) if days else 5
                        days = max(1, min(5, days))  # 1-5 범위로 제한
                        app.show_forecast(city, days)
                    except ValueError:
                        app.show_forecast(city)
            
            elif choice == '3':
                app.show_favorite_weather()
            
            elif choice == '4':
                city = input("즐겨찾기에 추가할 도시명 (영문): ").strip()
                if city:
                    app.add_favorite_city(city)
            
            elif choice == '5':
                if app.favorite_cities:
                    print("즐겨찾기 목록:")
                    for i, city in enumerate(app.favorite_cities, 1):
                        print(f"{i}. {city}")
                    
                    try:
                        index = int(input("제거할 도시 번호: ")) - 1
                        if 0 <= index < len(app.favorite_cities):
                            city = app.favorite_cities[index]
                            app.remove_favorite_city(city)
                        else:
                            print("잘못된 번호입니다.")
                    except ValueError:
                        print("숫자를 입력해주세요.")
                else:
                    print("즐겨찾기 목록이 비어있습니다.")
            
            elif choice == '6':
                if app.favorite_cities:
                    print("즐겨찾는 도시 목록:")
                    for i, city in enumerate(app.favorite_cities, 1):
                        print(f"{i}. {city}")
                else:
                    print("즐겨찾는 도시가 없습니다.")
            
            elif choice == '7':
                print("프로그램을 종료합니다.")
                break
            
            else:
                print("잘못된 선택입니다.")
        
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    weather_app_demo()
```

---

## 종합 프로젝트

### 프로젝트: 웹 기반 일정 관리 시스템
이번 단계에서 배운 모든 내용을 종합하여 Flask를 이용한 웹 기반 일정 관리 시스템을 만들어보세요.

**기능 요구사항:**
1. 사용자 등록/로그인
2. 일정 CRUD (생성, 조회, 수정, 삭제)
3. 카테고리별 일정 관리
4. 일정 알림 기능
5. 월별/주별 캘린더 뷰
6. 일정 검색 기능
7. CSV 내보내기/가져오기

**기술 스택:**
- Backend: Flask
- Database: SQLite (SQLAlchemy ORM)
- Frontend: HTML, CSS, JavaScript
- Authentication: Flask-Login

이 프로젝트를 통해 객체지향 프로그래밍, 파일 처리, 라이브러리 활용, 웹 개발 등 중급 과정에서 학습한 모든 내용을 실전에 적용할 수 있습니다.

---

*중급 단계를 완주하셨다면 이제 실무 수준의 프로그래밍 역량을 갖추었습니다. 고급 과정으로 진행하여 더 전문적인 기술을 습득해보세요!*
