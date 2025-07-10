# 파이썬 설치 가이드

## 🖥 운영체제별 설치 방법

### Windows
1. **공식 사이트에서 다운로드**
   - [Python.org](https://www.python.org/downloads/)에서 최신 버전 다운로드
   - 설치 시 "Add Python to PATH" 체크박스 선택

2. **Microsoft Store에서 설치**
   ```
   Microsoft Store 검색 → "Python 3.x" 설치
   ```

3. **설치 확인**
   ```cmd
   python --version
   pip --version
   ```

### macOS
1. **Homebrew 사용 (권장)**
   ```bash
   # Homebrew 설치 (미설치 시)
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Python 설치
   brew install python
   ```

2. **공식 인스톨러 사용**
   - [Python.org](https://www.python.org/downloads/)에서 macOS용 인스톨러 다운로드

### Linux (Ubuntu/Debian)
```bash
# 시스템 업데이트
sudo apt update

# Python 3 설치
sudo apt install python3 python3-pip

# 개발 도구 설치
sudo apt install python3-dev python3-venv
```

### Linux (CentOS/RHEL)
```bash
# Python 3 설치
sudo yum install python3 python3-pip

# 또는 dnf 사용 (최신 버전)
sudo dnf install python3 python3-pip
```

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