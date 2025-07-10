# 🔧 초보자를 위한 문제 해결 가이드

## 🚨 가장 흔한 오류와 해결법

### 1. "python이 인식되지 않습니다" (Windows)

**문제**: 파이썬을 설치했는데 명령어가 인식되지 않아요.

**해결법**:
```cmd
# 1. 파이썬이 설치되어 있는지 확인
where python

# 2. PATH에 추가되어 있는지 확인
echo %PATH%
```

**해결 방법**:
1. 파이썬을 다시 설치할 때 "Add Python to PATH" 체크박스 선택
2. 또는 수동으로 PATH 추가:
   - 시작 → 시스템 환경 변수 편집
   - 환경 변수 → Path → 편집
   - 파이썬 설치 경로 추가 (예: `C:\Python39\`)

### 2. "SyntaxError: invalid syntax"

**문제**: 코드를 실행할 때 문법 오류가 나요.

**흔한 원인들**:
```python
# ❌ 잘못된 예시
print "Hello"  # Python 3에서는 괄호 필요

if x = 5:  # 할당(=) 대신 비교(==) 사용해야 함
    print("x is 5")

print("Hello"  # 닫는 괄호 누락

# ✅ 올바른 예시
print("Hello")

if x == 5:
    print("x is 5")

print("Hello")
```

### 3. "IndentationError: expected an indented block"

**문제**: 들여쓰기 오류가 나요.

**해결법**:
```python
# ❌ 잘못된 예시
if True:
print("Hello")  # 들여쓰기 없음

# ✅ 올바른 예시
if True:
    print("Hello")  # 4칸 또는 Tab으로 들여쓰기
```

**팁**: 
- VS Code에서 Tab 키를 스페이스로 설정하기
- 들여쓰기는 일관성 있게 4칸 또는 Tab 사용

### 4. "NameError: name 'x' is not defined"

**문제**: 변수를 사용했는데 정의되지 않았다고 나와요.

**흔한 원인들**:
```python
# ❌ 잘못된 예시
print(name)  # name 변수를 정의하지 않음

# ✅ 올바른 예시
name = "파이썬"
print(name)

# ❌ 오타
nmae = "파이썬"  # name으로 써야 함
print(name)

# ✅ 올바른 예시
name = "파이썬"
print(name)
```

### 5. "ModuleNotFoundError: No module named 'xxx'"

**문제**: 라이브러리를 import 할 수 없어요.

**해결법**:
```bash
# 패키지 설치
pip install 패키지명

# 예시
pip install requests
pip install pandas

# 가상환경에서 설치 (권장)
pip install --user 패키지명
```

### 6. "TypeError: 'str' object cannot be interpreted as an integer"

**문제**: 문자열을 숫자로 사용하려고 해요.

**해결법**:
```python
# ❌ 잘못된 예시
age = input("나이를 입력하세요: ")  # input()은 항상 문자열 반환
if age > 18:  # 문자열과 숫자 비교 불가
    print("성인입니다")

# ✅ 올바른 예시
age = int(input("나이를 입력하세요: "))  # 문자열을 정수로 변환
if age > 18:
    print("성인입니다")
```

## 💡 디버깅 팁

### 1. print()로 값 확인하기
```python
# 변수 값 확인
x = 10
print(f"x의 값: {x}")
print(f"x의 타입: {type(x)}")

# 조건문 확인
if x > 5:
    print("조건문 통과!")  # 이 메시지가 나오는지 확인
```

### 2. 한 줄씩 실행해보기
```python
# 복잡한 코드를 단계별로 나누어 실행
numbers = [1, 2, 3, 4, 5]
print(numbers)  # 1단계: 리스트 확인

total = 0
print(f"초기 total: {total}")  # 2단계: 초기값 확인

for num in numbers:
    total += num
    print(f"num: {num}, total: {total}")  # 3단계: 각 단계별 값 확인
```

### 3. 에러 메시지 읽는 법
```
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

**읽는 순서**:
1. **파일명과 줄 번호**: `File "test.py", line 5`
2. **에러 종류**: `ZeroDivisionError`
3. **에러 설명**: `division by zero`

## 🆘 막혔을 때 도움 받는 방법

### 1. 구글링 팁
```
파이썬 + 에러메시지 + 한국어
예: "파이썬 NameError 해결"
예: "python SyntaxError invalid syntax"
```

### 2. 유용한 사이트들
- **Stack Overflow**: 세계 최대 프로그래밍 Q&A 사이트
- **파이썬 공식 문서**: https://docs.python.org/ko/3/
- **점프 투 파이썬**: https://wikidocs.net/book/1

### 3. 질문하는 방법
**좋은 질문 형식**:
```
제목: 파이썬 초보 - 변수 선언 오류 질문

내용:
안녕하세요. 파이썬을 배우기 시작한 초보자입니다.

다음 코드를 실행했는데 오류가 나네요:
[코드 붙여넣기]

오류 메시지:
[오류 메시지 붙여넣기]

어떤 부분이 잘못된 건지 알려주세요.
```

## 🎯 자주 실수하는 포인트

### 1. 들여쓰기
- **규칙**: 4칸 또는 Tab 일관성 있게 사용
- **확인법**: VS Code에서 들여쓰기 표시 활성화

### 2. 변수명 규칙
```python
# ❌ 잘못된 변수명
2name = "파이썬"  # 숫자로 시작 불가
my-name = "파이썬"  # 하이픈 사용 불가
my name = "파이썬"  # 공백 사용 불가

# ✅ 올바른 변수명
my_name = "파이썬"
myName = "파이썬"
name2 = "파이썬"
```

### 3. 함수 호출 시 괄호 빼먹기
```python
# ❌ 잘못된 예시
print "Hello"  # 괄호 없음
len("Hello")  # 결과를 사용하지 않음

# ✅ 올바른 예시
print("Hello")  # 괄호 포함
length = len("Hello")  # 결과를 변수에 저장
```

## 🔍 개발 도구 활용하기

### VS Code 디버깅
1. **중단점 설정**: 코드 줄 번호 왼쪽 클릭
2. **F5**: 디버깅 시작
3. **F10**: 한 줄씩 실행
4. **변수 확인**: 왼쪽 패널에서 변수 값 실시간 확인

### Python 대화형 모드 활용
```bash
# 터미널에서 Python 실행
python

# 간단한 계산이나 테스트
>>> 2 + 3
5
>>> x = "Hello"
>>> print(x)
Hello
>>> exit()  # 종료
```

## 📞 더 많은 도움이 필요하다면

- **파이썬 코리아 커뮤니티**: https://www.facebook.com/groups/pythonkorea/
- **OKKY**: https://okky.kr/
- **인프런 질문/답변**: https://www.inflearn.com/questions
- **GitHub Issues**: 이 저장소에서 질문하기

---

**💪 기억하세요**: 에러는 배움의 기회입니다! 모든 개발자가 거쳐가는 과정이니 좌절하지 말고 차근차근 해결해나가세요.