# 파이썬 학습 로드맵 상세 가이드

## 📋 목차
1. [학습 전 준비사항](#학습-전-준비사항)
2. [초급 단계 (1-2개월)](#초급-단계-1-2개월)
3. [중급 단계 (2-3개월)](#중급-단계-2-3개월)
4. [고급 단계 (3-4개월)](#고급-단계-3-4개월)
5. [전문가 단계 (지속적)](#전문가-단계-지속적)

---

## 학습 전 준비사항

### 📋 체크리스트
- [ ] 파이썬 3.8 이상 설치
- [ ] 코드 에디터 설치 (VS Code, PyCharm 등)
- [ ] Git 기초 이해
- [ ] 학습 시간 계획 수립 (일 1-2시간 권장)

### 🛠 개발 환경 설정
```bash
# 파이썬 버전 확인
python --version

# pip 업그레이드
pip install --upgrade pip

# 가상환경 생성
python -m venv python_study
source python_study/bin/activate  # Linux/Mac
# python_study\Scripts\activate  # Windows
```

---

## 초급 단계 (1-2개월)

### 🎯 학습 목표
파이썬의 기본 문법을 익히고 간단한 프로그램을 작성할 수 있다.

### 📚 1주차: 파이썬 기초
**학습 내용:**
- [ ] 파이썬 소개와 특징
- [ ] 변수와 데이터 타입
- [ ] 기본 연산자
- [ ] 입출력 함수 (print, input)

**실습 과제:**
1. 자기소개 프로그램 만들기
2. 계산기 프로그램 만들기
3. 단위 변환 프로그램 (온도, 길이 등)

**예제 코드:**
```python
# 1. 자기소개 프로그램
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
print(f"안녕하세요! 저는 {name}이고, {age}살입니다.")

# 2. 간단한 계산기
num1 = float(input("첫 번째 숫자: "))
num2 = float(input("두 번째 숫자: "))
print(f"덧셈: {num1 + num2}")
print(f"뺄셈: {num1 - num2}")
print(f"곱셈: {num1 * num2}")
print(f"나눗셈: {num1 / num2}")
```

### 📚 2주차: 제어문
**학습 내용:**
- [ ] 조건문 (if, elif, else)
- [ ] 반복문 (for, while)
- [ ] break, continue
- [ ] 중첩 구조

**실습 과제:**
1. 숫자 맞추기 게임
2. 구구단 출력 프로그램
3. 성적 등급 계산기

**예제 코드:**
```python
# 숫자 맞추기 게임
import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("1부터 100까지 숫자를 맞춰보세요: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"정답! {attempts}번 만에 맞췄습니다!")
        break
    elif guess < secret_number:
        print("더 큰 숫자입니다.")
    else:
        print("더 작은 숫자입니다.")
```

### 📚 3주차: 자료구조
**학습 내용:**
- [ ] 리스트 (List)
- [ ] 튜플 (Tuple)
- [ ] 딕셔너리 (Dictionary)
- [ ] 집합 (Set)

**실습 과제:**
1. 학생 성적 관리 시스템
2. 쇼핑 카트 프로그램
3. 전화번호부 만들기

### 📚 4주차: 함수와 모듈
**학습 내용:**
- [ ] 함수 정의와 호출
- [ ] 매개변수와 반환값
- [ ] 지역변수와 전역변수
- [ ] 모듈 import

**실습 과제:**
1. 다양한 계산 함수 모음
2. 문자열 처리 함수
3. 간단한 게임 함수

---

## 중급 단계 (2-3개월)

### 🎯 학습 목표
객체지향 프로그래밍을 이해하고 실용적인 프로그램을 개발할 수 있다.

### 📚 5-6주차: 객체지향 프로그래밍
**학습 내용:**
- [ ] 클래스와 객체
- [ ] 생성자와 소멸자
- [ ] 상속과 다형성
- [ ] 캡슐화

**실습 과제:**
1. 은행 계좌 관리 시스템
2. 도서관 관리 시스템
3. 간단한 RPG 게임

**예제 코드:**
```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"입금: {amount}원")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"출금: {amount}원")
            return True
        return False
    
    def get_balance(self):
        return self.balance
```

### 📚 7-8주차: 파일 처리와 예외 처리
**학습 내용:**
- [ ] 파일 읽기/쓰기
- [ ] CSV, JSON 파일 처리
- [ ] try-except 문
- [ ] 사용자 정의 예외

**실습 과제:**
1. 일기장 프로그램
2. 주소록 관리 (CSV)
3. 설정 파일 관리 (JSON)

### 📚 9-10주차: 라이브러리 활용
**학습 내용:**
- [ ] 표준 라이브러리 (datetime, os, sys)
- [ ] 서드파티 라이브러리 (requests, pandas)
- [ ] pip 사용법
- [ ] 가상환경 관리

**실습 과제:**
1. 날씨 정보 조회 프로그램
2. 웹 페이지 정보 수집
3. 데이터 분석 기초

---

## 고급 단계 (3-4개월)

### 🎯 학습 목표
웹 개발, 데이터베이스, API 개발 등 실무 수준의 기술을 습득한다.

### 📚 11-12주차: 웹 프레임워크 기초
**학습 내용:**
- [ ] Flask 기초
- [ ] 라우팅과 템플릿
- [ ] 폼 처리
- [ ] 세션과 쿠키

**실습 과제:**
1. 개인 블로그 만들기
2. 할 일 목록 웹 앱
3. 간단한 쇼핑몰

### 📚 13-14주차: 데이터베이스 연동
**학습 내용:**
- [ ] SQLite 기초
- [ ] SQL 쿼리
- [ ] ORM (SQLAlchemy)
- [ ] 데이터 마이그레이션

**실습 과제:**
1. 사용자 관리 시스템
2. 게시판 기능
3. 상품 재고 관리

### 📚 15-16주차: API 개발
**학습 내용:**
- [ ] RESTful API 설계
- [ ] JSON 데이터 처리
- [ ] 인증과 권한
- [ ] API 테스팅

**실습 과제:**
1. 사용자 인증 API
2. 게시글 CRUD API
3. 파일 업로드 API

---

## 전문가 단계 (지속적)

### 🎯 학습 목표
전문 개발자로서 고급 기술과 모범 사례를 적용한다.

### 📚 심화 학습 영역

**웹 개발**
- [ ] Django 프레임워크
- [ ] 비동기 프로그래밍 (AsyncIO)
- [ ] 마이크로서비스 아키텍처
- [ ] 컨테이너화 (Docker)

**데이터 사이언스**
- [ ] NumPy, Pandas 고급 활용
- [ ] 데이터 시각화 (Matplotlib, Seaborn)
- [ ] 머신러닝 (Scikit-learn)
- [ ] 딥러닝 기초 (TensorFlow, PyTorch)

**DevOps & 배포**
- [ ] CI/CD 파이프라인
- [ ] 클라우드 서비스 (AWS, GCP)
- [ ] 모니터링과 로깅
- [ ] 성능 최적화

---

## 📈 학습 평가 및 피드백

### 주간 체크리스트
매주 다음 항목들을 점검하세요:
- [ ] 이론 학습 완료
- [ ] 실습 과제 완료
- [ ] 코드 리뷰 및 개선
- [ ] 다음 주 학습 계획 수립

### 월간 프로젝트
각 단계별로 종합 프로젝트를 진행하세요:
- **초급**: 개인 가계부 프로그램
- **중급**: 웹 기반 일정 관리 시스템
- **고급**: 전자상거래 플랫폼 MVP

---

## 🎯 학습 팁

1. **꾸준함이 핵심**: 매일 조금씩이라도 코딩하기
2. **실습 중심**: 이론보다는 직접 코드 작성하기
3. **프로젝트 만들기**: 배운 내용을 종합해서 프로젝트 완성하기
4. **커뮤니티 참여**: 온라인 포럼이나 스터디 그룹 활용하기
5. **코드 리뷰**: 다른 사람의 코드 읽고 배우기

## 🔗 다음 단계

이 로드맵을 완주한 후에는:
- 오픈소스 프로젝트 기여
- 개인 포트폴리오 구축
- 기술 블로그 운영
- 네트워킹 및 커뮤니티 활동

---

*"프로그래밍은 마라톤입니다. 꾸준히, 즐겁게 학습하세요!"*