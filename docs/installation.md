# 🐍 파이썬 설치 가이드

**🎯 목표**: 파이썬을 설치하고 첫 프로그램을 실행할 수 있도록!

> **완전 초보자라면?** 걱정 마세요! 이 가이드는 컴퓨터를 잘 모르는 분도 따라할 수 있게 만들어졌어요.

## 🚀 빠른 설치 (권장)

### 🪟 Windows 사용자
1. **Microsoft Store** 열기 (시작 메뉴에서 검색)
2. **"Python"** 검색해서 최신 버전 설치
3. **설치 완료!** ✅

### 🍎 Mac 사용자  
1. **[python.org](https://www.python.org/downloads/)** 접속
2. **"Download Python"** 큰 버튼 클릭
3. **다운로드된 파일 실행해서 설치**
4. **설치 완료!** ✅

## ✅ 설치 확인하기

설치가 완료되었는지 확인해볼까요?

### Windows
1. `Win + R` 키 → `cmd` 입력 → 엔터
2. 다음 명령어 입력:
```cmd
python --version
```

### Mac/Linux
1. 터미널 열기 (`Cmd + Space` → "터미널" 검색)
2. 다음 명령어 입력:
```bash
python3 --version
```

**결과**: `Python 3.x.x` 같은 메시지가 나오면 성공! 🎉

### 안 될 때는?
- Windows에서 `python`이 인식 안 됨 → `py` 명령어 시도
- 그래도 안 됨 → [상세 설치 가이드](#상세-설치-방법) 참고

## 🎯 첫 프로그램 실행해보기

설치 확인이 끝났다면 바로 첫 프로그램을 만들어봅시다!

### 1단계: 메모장 열기 (Windows) 또는 텍스트편집 (Mac)

### 2단계: 다음 코드 입력
```python
print("안녕하세요! 파이썬 설치 성공! 🐍")
print("첫 번째 프로그램이 실행되었습니다!")
```

### 3단계: 파일 저장
- 파일명: `test.py` 
- 위치: 바탕화면
- **중요**: 확장자를 반드시 `.py`로!

### 4단계: 실행하기
```bash
# 바탕화면으로 이동
cd Desktop

# 프로그램 실행
python test.py
```

**성공!** 메시지가 나왔다면 설치 완료! 🎊

## 📱 더 편한 도구 설치하기 (선택사항)

### VS Code (무료, 강력 추천!)
1. **[code.visualstudio.com](https://code.visualstudio.com/)** 접속
2. **Download** 클릭해서 설치
3. **Python Extension** 설치 ([설치 방법](#vs-code-설정))

### 왜 VS Code를 써야 하나요?
- ✅ **자동 완성**: 코드를 반만 쳐도 추천해줌
- ✅ **에러 표시**: 실수를 미리 찾아줌  
- ✅ **예쁜 색깔**: 코드가 읽기 쉬워짐
- ✅ **무료**: 돈 안 내고 계속 사용!

---

## 🛠 개발 환경 설정

### 1. 코드 에디터 선택

**VS Code (추천)**
- 무료, 가벼움, 풍부한 확장 기능
- Python Extension 설치 필수
- [다운로드](https://code.visualstudio.com/)

**PyCharm**
- 강력한 IDE, 디버깅 기능 우수
- Community Edition (무료) / Professional Edition (유료)
- [다운로드](https://www.jetbrains.com/pycharm/)

**기타 에디터**
- Sublime Text
- Atom
- Vim/Neovim

### 2. 필수 VS Code 확장 프로그램
```
- Python (Microsoft)
- Python Docstring Generator
- autoDocstring
- Python Indent
- Pylance
- GitLens
```

### 3. 가상환경 설정
```bash
# 가상환경 생성
python -m venv my_project

# 활성화 (Windows)
my_project\Scripts\activate

# 활성화 (macOS/Linux)
source my_project/bin/activate

# 비활성화
deactivate
```

---

## 📦 패키지 관리

### pip 기본 사용법
```bash
# 패키지 설치
pip install package_name

# 특정 버전 설치
pip install package_name==1.0.0

# requirements.txt에서 설치
pip install -r requirements.txt

# 설치된 패키지 목록
pip list

# 패키지 정보 확인
pip show package_name

# 패키지 업그레이드
pip install --upgrade package_name

# 패키지 제거
pip uninstall package_name
```

### requirements.txt 만들기
```bash
# 현재 환경의 패키지 목록 저장
pip freeze > requirements.txt
```

---

## 🔧 개발 도구 설치

### 기본 개발 패키지
```bash
pip install --upgrade pip setuptools wheel
```

### 코드 품질 도구
```bash
# 코드 포맷터
pip install black

# 린터
pip install flake8 pylint

# 타입 체커
pip install mypy
```

### 테스팅 도구
```bash
pip install pytest pytest-cov
```

---

## 🐛 일반적인 설치 문제 해결

### Windows 관련 문제

**문제**: 'python'이 인식되지 않음
**해결**: 
1. 시스템 환경 변수 PATH에 Python 경로 추가
2. 재설치 시 "Add Python to PATH" 체크

**문제**: pip 설치 오류
**해결**:
```cmd
python -m ensurepip --upgrade
```

### macOS 관련 문제

**문제**: SSL 인증서 오류
**해결**:
```bash
/Applications/Python\ 3.x/Install\ Certificates.command
```

### Linux 관련 문제

**문제**: 권한 오류
**해결**:
```bash
# 사용자 디렉토리에 설치
pip install --user package_name
```

---

## ✅ 설치 확인 체크리스트

설치 완료 후 다음 명령어들이 정상 작동하는지 확인하세요:

```bash
# Python 버전 확인
python --version
# 또는
python3 --version

# pip 버전 확인
pip --version
# 또는
pip3 --version

# Python 대화형 모드 실행
python
>>> print("Hello, Python!")
>>> exit()

# 간단한 스크립트 실행
echo 'print("설치 완료!")' > test.py
python test.py
```

---

## 📚 추가 학습 자료

### 공식 문서
- [Python 공식 문서](https://docs.python.org/ko/3/)
- [Python Tutorial](https://docs.python.org/ko/3/tutorial/)

### 온라인 학습 플랫폼
- [점프 투 파이썬](https://wikidocs.net/book/1)
- [Python.org 한국어 튜토리얼](https://docs.python.org/ko/3/tutorial/)
- [코딩도장 파이썬](https://dojang.io/course/view.php?id=7)

---

*설치가 완료되면 [학습 로드맵](../python-roadmap.md)을 따라 학습을 시작하세요!*