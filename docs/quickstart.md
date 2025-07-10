# ⚡ 5분 퀵스타트 - 첫 파이썬 프로그램 만들기

**🎯 목표**: 파이썬 설치부터 첫 프로그램 실행까지 5분 안에 완성하기!

## 🚀 1단계: 파이썬 설치 확인 (1분)

### Windows
1. `Win + R` 키를 눌러 실행창 열기
2. `cmd` 입력 후 엔터
3. 다음 명령어 입력:
```cmd
python --version
```

### Mac/Linux
1. 터미널 열기 (`Cmd + Space` → "터미널" 검색)
2. 다음 명령어 입력:
```bash
python3 --version
```

**결과가 `Python 3.x.x`로 나오면 설치 완료!**  
**안 나오면** → [설치 가이드](installation.md) 참고

## 👋 2단계: 첫 번째 프로그램 (2분)

### 메모장이나 VS Code에서 다음 코드 작성:

```python
# hello.py
print("안녕하세요! 저는 파이썬입니다! 🐍")
print("첫 번째 프로그램을 성공적으로 만들었네요!")

# 이제 계산도 해볼까요?
result = 2023 + 1
print(f"올해는 {result}년이에요!")

# 나의 정보 입력받기
name = input("당신의 이름은 무엇인가요? ")
print(f"안녕하세요, {name}님! 파이썬 학습을 환영합니다! 🎉")
```

### 파일 저장:
- 파일명: `hello.py` (확장자 `.py` 중요!)
- 위치: 바탕화면이나 원하는 폴더

## ▶️ 3단계: 프로그램 실행 (1분)

### Windows:
```cmd
cd Desktop  # 바탕화면에 저장했다면
python hello.py
```

### Mac/Linux:
```bash
cd Desktop  # 바탕화면에 저장했다면
python3 hello.py
```

## 🎮 4단계: 재미있는 게임 만들기 (1분)

```python
# game.py
import random

print("🎲 숫자 맞추기 게임에 오신 것을 환영합니다!")
secret = random.randint(1, 10)

while True:
    guess = int(input("1부터 10까지 숫자를 맞춰보세요: "))
    
    if guess == secret:
        print("🎉 정답입니다! 축하해요!")
        break
    elif guess < secret:
        print("⬆️ 더 큰 숫자예요!")
    else:
        print("⬇️ 더 작은 숫자예요!")

print("게임 끝! 파이썬 재미있죠? 😊")
```

## 🏆 축하합니다! 성공!

이제 여러분은:
- ✅ 파이썬 프로그램을 실행할 수 있어요
- ✅ 변수와 출력을 사용할 수 있어요  
- ✅ 사용자 입력을 받을 수 있어요
- ✅ 간단한 게임을 만들 수 있어요

## 🎯 다음 단계는?

### 🌱 초보자 코스 시작하기
1. **[상세 학습 로드맵](../python-roadmap.md)** - 체계적인 학습 계획
2. **[초급 예제들](../examples/beginner/)** - 더 많은 실습 프로젝트

### 💡 더 만들어볼 것들
```python
# 간단한 계산기
num1 = float(input("첫 번째 숫자: "))
num2 = float(input("두 번째 숫자: "))
print(f"더하기: {num1 + num2}")
print(f"빼기: {num1 - num2}")
print(f"곱하기: {num1 * num2}")
print(f"나누기: {num1 / num2}")
```

```python
# 나이 계산기
birth_year = int(input("태어난 년도를 입력하세요: "))
current_year = 2024
age = current_year - birth_year
print(f"당신의 나이는 {age}살입니다!")

if age >= 20:
    print("성인이시네요! 🎓")
else:
    print("아직 미성년자시군요! 👶")
```

## 🆘 문제가 생겼다면?

- **오류 메시지가 나와요** → [문제 해결 가이드](troubleshooting.md)
- **더 배우고 싶어요** → [FAQ](faq.md)
- **막혔어요** → GitHub Issues에 질문하기

---

**🎉 첫 파이썬 프로그램 완성을 축하드려요!** 

이제 프로그래밍의 세계에 첫 발을 내디뎠습니다. 계속해서 재미있는 것들을 만들어보세요! 🚀