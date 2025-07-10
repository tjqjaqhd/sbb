# 초급자 실습 예제

## 📝 목차
1. [1주차: 기초 문법](#1주차-기초-문법)
2. [2주차: 제어문](#2주차-제어문)
3. [3주차: 자료구조](#3주차-자료구조)
4. [4주차: 함수](#4주차-함수)

---

## 1주차: 기초 문법

### 예제 1: 자기소개 프로그램
```python
# intro.py
print("=== 자기소개 프로그램 ===")

name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
hobby = input("취미를 입력하세요: ")

print(f"\n안녕하세요! 저는 {name}입니다.")
print(f"나이는 {age}살이고, 취미는 {hobby}입니다.")

# 10년 후 나이 계산
future_age = age + 10
print(f"10년 후에는 {future_age}살이 되겠네요!")
```

### 예제 2: 단위 변환 계산기
```python
# converter.py
print("=== 단위 변환 계산기 ===")
print("1. 섭씨 → 화씨")
print("2. 화씨 → 섭씨") 
print("3. cm → inch")
print("4. inch → cm")

choice = int(input("변환할 항목을 선택하세요 (1-4): "))

if choice == 1:
    celsius = float(input("섭씨온도를 입력하세요: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
    
elif choice == 2:
    fahrenheit = float(input("화씨온도를 입력하세요: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
    
elif choice == 3:
    cm = float(input("cm를 입력하세요: "))
    inch = cm / 2.54
    print(f"{cm}cm = {inch:.2f}inch")
    
elif choice == 4:
    inch = float(input("inch를 입력하세요: "))
    cm = inch * 2.54
    print(f"{inch}inch = {cm:.2f}cm")
    
else:
    print("잘못된 선택입니다.")
```

### 예제 3: 간단한 계산기
```python
# calculator.py
print("=== 간단한 계산기 ===")

num1 = float(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
num2 = float(input("두 번째 숫자를 입력하세요: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("0으로 나눌 수 없습니다!")
        exit()
else:
    print("잘못된 연산자입니다!")
    exit()

print(f"{num1} {operator} {num2} = {result}")
```

---

## 2주차: 제어문

### 예제 4: 숫자 맞추기 게임
```python
# guess_number.py
import random

print("=== 숫자 맞추기 게임 ===")
print("1부터 100까지의 숫자를 맞춰보세요!")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    try:
        guess = int(input(f"숫자를 입력하세요 (남은 기회: {max_attempts - attempts}): "))
        attempts += 1
        
        if guess == secret_number:
            print(f"축하합니다! {attempts}번 만에 맞췄습니다!")
            break
        elif guess < secret_number:
            print("더 큰 숫자입니다.")
        else:
            print("더 작은 숫자입니다.")
            
    except ValueError:
        print("숫자만 입력해주세요!")
        attempts -= 1  # 잘못된 입력은 횟수에 포함하지 않음
        
else:
    print(f"게임 오버! 정답은 {secret_number}였습니다.")
```

### 예제 5: 구구단 출력 프로그램
```python
# multiplication_table.py
print("=== 구구단 프로그램 ===")
print("1. 특정 단 출력")
print("2. 전체 구구단 출력")
print("3. 구구단 게임")

choice = int(input("선택하세요 (1-3): "))

if choice == 1:
    dan = int(input("몇 단을 출력할까요? "))
    print(f"\n{dan}단:")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")
        
elif choice == 2:
    print("\n전체 구구단:")
    for dan in range(2, 10):
        print(f"\n{dan}단:")
        for i in range(1, 10):
            print(f"{dan} × {i} = {dan * i}")
            
elif choice == 3:
    print("\n구구단 게임 시작!")
    score = 0
    total_questions = 5
    
    for _ in range(total_questions):
        num1 = random.randint(2, 9)
        num2 = random.randint(1, 9)
        correct_answer = num1 * num2
        
        user_answer = int(input(f"{num1} × {num2} = ? "))
        
        if user_answer == correct_answer:
            print("정답!")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 {correct_answer}입니다.")
    
    print(f"\n게임 종료! 점수: {score}/{total_questions}")
```

### 예제 6: 성적 관리 프로그램
```python
# grade_manager.py
print("=== 성적 관리 프로그램 ===")

students = []

while True:
    print("\n1. 학생 추가")
    print("2. 성적 조회")
    print("3. 전체 성적 보기")
    print("4. 종료")
    
    choice = input("선택하세요: ")
    
    if choice == '1':
        name = input("학생 이름: ")
        korean = int(input("국어 점수: "))
        english = int(input("영어 점수: "))
        math = int(input("수학 점수: "))
        
        total = korean + english + math
        average = total / 3
        
        # 등급 계산
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'
            
        student = {
            'name': name,
            'korean': korean,
            'english': english,
            'math': math,
            'total': total,
            'average': average,
            'grade': grade
        }
        
        students.append(student)
        print(f"{name} 학생이 추가되었습니다.")
        
    elif choice == '2':
        name = input("조회할 학생 이름: ")
        found = False
        
        for student in students:
            if student['name'] == name:
                print(f"\n{name} 학생의 성적:")
                print(f"국어: {student['korean']}")
                print(f"영어: {student['english']}")
                print(f"수학: {student['math']}")
                print(f"총점: {student['total']}")
                print(f"평균: {student['average']:.2f}")
                print(f"등급: {student['grade']}")
                found = True
                break
                
        if not found:
            print("해당 학생을 찾을 수 없습니다.")
            
    elif choice == '3':
        if not students:
            print("등록된 학생이 없습니다.")
        else:
            print("\n전체 학생 성적:")
            print("이름\t국어\t영어\t수학\t총점\t평균\t등급")
            print("-" * 50)
            for student in students:
                print(f"{student['name']}\t{student['korean']}\t{student['english']}\t{student['math']}\t{student['total']}\t{student['average']:.2f}\t{student['grade']}")
                
    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
        
    else:
        print("잘못된 선택입니다.")
```

---

## 3주차: 자료구조

### 예제 7: 쇼핑 카트 프로그램
```python
# shopping_cart.py
print("=== 쇼핑 카트 프로그램 ===")

# 상품 목록 (딕셔너리)
products = {
    1: {"name": "사과", "price": 1000},
    2: {"name": "바나나", "price": 1500},
    3: {"name": "오렌지", "price": 2000},
    4: {"name": "포도", "price": 3000},
    5: {"name": "딸기", "price": 2500}
}

cart = []  # 장바구니 (리스트)

while True:
    print("\n=== 상품 목록 ===")
    for product_id, info in products.items():
        print(f"{product_id}. {info['name']} - {info['price']}원")
    
    print("\n1. 상품 추가")
    print("2. 장바구니 보기")
    print("3. 상품 제거")
    print("4. 결제하기")
    print("5. 종료")
    
    choice = input("선택하세요: ")
    
    if choice == '1':
        try:
            product_id = int(input("추가할 상품 번호: "))
            if product_id in products:
                quantity = int(input("수량: "))
                
                # 이미 장바구니에 있는지 확인
                found = False
                for item in cart:
                    if item['id'] == product_id:
                        item['quantity'] += quantity
                        found = True
                        break
                
                if not found:
                    cart.append({
                        'id': product_id,
                        'name': products[product_id]['name'],
                        'price': products[product_id]['price'],
                        'quantity': quantity
                    })
                
                print(f"{products[product_id]['name']} {quantity}개가 장바구니에 추가되었습니다.")
            else:
                print("잘못된 상품 번호입니다.")
        except ValueError:
            print("숫자를 입력해주세요.")
    
    elif choice == '2':
        if not cart:
            print("장바구니가 비어있습니다.")
        else:
            print("\n=== 장바구니 ===")
            total_price = 0
            for item in cart:
                subtotal = item['price'] * item['quantity']
                print(f"{item['name']} - {item['price']}원 × {item['quantity']}개 = {subtotal}원")
                total_price += subtotal
            print(f"\n총 금액: {total_price}원")
    
    elif choice == '3':
        if not cart:
            print("장바구니가 비어있습니다.")
        else:
            print("\n=== 장바구니 ===")
            for i, item in enumerate(cart):
                print(f"{i+1}. {item['name']} × {item['quantity']}개")
            
            try:
                index = int(input("제거할 상품 번호: ")) - 1
                if 0 <= index < len(cart):
                    removed_item = cart.pop(index)
                    print(f"{removed_item['name']}이(가) 제거되었습니다.")
                else:
                    print("잘못된 번호입니다.")
            except ValueError:
                print("숫자를 입력해주세요.")
    
    elif choice == '4':
        if not cart:
            print("장바구니가 비어있습니다.")
        else:
            print("\n=== 결제 내역 ===")
            total_price = 0
            for item in cart:
                subtotal = item['price'] * item['quantity']
                print(f"{item['name']} - {item['price']}원 × {item['quantity']}개 = {subtotal}원")
                total_price += subtotal
            
            print(f"\n총 결제 금액: {total_price}원")
            confirm = input("결제하시겠습니까? (y/n): ")
            
            if confirm.lower() == 'y':
                print("결제가 완료되었습니다!")
                cart.clear()  # 장바구니 비우기
            else:
                print("결제가 취소되었습니다.")
    
    elif choice == '5':
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("잘못된 선택입니다.")
```

---

## 4주차: 함수

### 예제 8: 함수 활용 프로그램
```python
# function_examples.py

def greet(name, age=None):
    """인사 함수"""
    if age:
        return f"안녕하세요, {name}님! {age}살이시군요."
    else:
        return f"안녕하세요, {name}님!"

def calculate_bmi(weight, height):
    """BMI 계산 함수"""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        status = "저체중"
    elif bmi < 25:
        status = "정상체중"
    elif bmi < 30:
        status = "과체중"
    else:
        status = "비만"
    
    return bmi, status

def get_max_min(numbers):
    """리스트에서 최대값, 최소값 찾기"""
    if not numbers:
        return None, None
    
    max_val = max(numbers)
    min_val = min(numbers)
    return max_val, min_val

def factorial(n):
    """팩토리얼 계산 (재귀함수)"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(num):
    """소수 판별 함수"""
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    """메인 함수"""
    print("=== 함수 활용 프로그램 ===")
    
    while True:
        print("\n1. 인사하기")
        print("2. BMI 계산")
        print("3. 최대값/최소값 찾기")
        print("4. 팩토리얼 계산")
        print("5. 소수 판별")
        print("6. 종료")
        
        choice = input("선택하세요: ")
        
        if choice == '1':
            name = input("이름을 입력하세요: ")
            age_input = input("나이를 입력하세요 (생략하려면 엔터): ")
            
            if age_input:
                age = int(age_input)
                message = greet(name, age)
            else:
                message = greet(name)
            
            print(message)
        
        elif choice == '2':
            try:
                weight = float(input("체중을 입력하세요 (kg): "))
                height = float(input("키를 입력하세요 (m): "))
                
                bmi, status = calculate_bmi(weight, height)
                print(f"BMI: {bmi:.2f}, 상태: {status}")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
        
        elif choice == '3':
            try:
                numbers_input = input("숫자들을 쉼표로 구분해서 입력하세요: ")
                numbers = [float(x.strip()) for x in numbers_input.split(',')]
                
                max_val, min_val = get_max_min(numbers)
                print(f"최대값: {max_val}, 최소값: {min_val}")
            except ValueError:
                print("올바른 숫자들을 입력해주세요.")
        
        elif choice == '4':
            try:
                n = int(input("팩토리얼을 계산할 숫자를 입력하세요: "))
                if n >= 0:
                    result = factorial(n)
                    print(f"{n}! = {result}")
                else:
                    print("0 이상의 숫자를 입력해주세요.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
        
        elif choice == '5':
            try:
                num = int(input("소수인지 확인할 숫자를 입력하세요: "))
                if is_prime(num):
                    print(f"{num}은(는) 소수입니다.")
                else:
                    print(f"{num}은(는) 소수가 아닙니다.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
        
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
```

---

## 📝 실습 과제

### 개인 프로젝트: 개인 가계부 프로그램
위에서 배운 내용들을 종합해서 간단한 가계부 프로그램을 만들어보세요.

**기능 요구사항:**
1. 수입/지출 내역 추가
2. 카테고리별 분류 (식비, 교통비, 문화생활 등)
3. 날짜별 조회
4. 월별 통계
5. 잔액 계산

**도전 과제:**
- 파일에 데이터 저장/불러오기 (CSV 형식)
- 그래프로 지출 내역 시각화 (matplotlib 사용)

---

*이 예제들을 직접 실행해보고, 코드를 수정해가며 이해도를 높여보세요!*