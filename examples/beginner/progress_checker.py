#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📊 파이썬 학습 진도 체커

이 프로그램으로 여러분의 파이썬 학습 진도를 확인해보세요!

📚 배우는 내용:
- 딕셔너리를 활용한 데이터 관리
- 반복문으로 진도 체크
- 퍼센트 계산
- 사용자 인터페이스 구성
"""

def display_progress(skills, category_name):
    """진도를 시각적으로 표시하는 함수"""
    completed = sum(1 for skill in skills.values() if skill)
    total = len(skills)
    percentage = (completed / total) * 100
    
    print(f"\n{category_name} 진도: {completed}/{total} ({percentage:.1f}%)")
    
    # 진도바 표시
    bar_length = 20
    filled_length = int(bar_length * completed // total)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    print(f"[{bar}] {percentage:.1f}%")
    
    return completed, total, percentage

def main():
    print("📊 파이썬 학습 진도 체커")
    print("=" * 40)
    print("각 항목을 완료했다면 'y', 아직이라면 'n'을 입력하세요!")
    
    # 초급 스킬 체크리스트
    beginner_skills = {
        "Hello World 프로그램 실행": False,
        "변수 선언하고 사용하기": False,
        "if문으로 조건 분기": False,
        "for/while문으로 반복": False,
        "함수 만들어서 사용": False,
        "간단한 계산기 완성": False
    }
    
    # 중급 스킬 체크리스트
    intermediate_skills = {
        "클래스 만들어서 객체 생성": False,
        "파일 읽기/쓰기": False,
        "try-except 에러 처리": False,
        "라이브러리 설치해서 사용": False,
        "웹 크롤링 기초": False,
        "실용적 프로그램 완성": False
    }
    
    # 고급 스킬 체크리스트
    advanced_skills = {
        "웹사이트 만들기 (Flask/Django)": False,
        "데이터베이스 사용": False,
        "API 만들고 사용하기": False,
        "Git으로 버전 관리": False,
        "서버에 배포하기": False,
        "포트폴리오 프로젝트 완성": False
    }
    
    # 사용자 입력 받기
    skill_sets = [
        (beginner_skills, "🌱 초급"),
        (intermediate_skills, "🌿 중급"),
        (advanced_skills, "🌳 고급")
    ]
    
    total_completed = 0
    total_skills = 0
    
    for skills, category in skill_sets:
        print(f"\n{category} 기술 체크:")
        print("-" * 30)
        
        for skill_name in skills:
            while True:
                response = input(f"✅ {skill_name} (y/n): ").lower().strip()
                if response in ['y', 'yes', '네', 'ㅇ']:
                    skills[skill_name] = True
                    break
                elif response in ['n', 'no', '아니오', 'ㄴ']:
                    skills[skill_name] = False
                    break
                else:
                    print("   'y' 또는 'n'을 입력해주세요!")
        
        # 진도 표시
        completed, total, percentage = display_progress(skills, category)
        total_completed += completed
        total_skills += total
    
    # 전체 진도 계산
    overall_percentage = (total_completed / total_skills) * 100
    
    print("\n" + "=" * 40)
    print("🎯 전체 학습 진도 요약")
    print("=" * 40)
    
    bar_length = 30
    filled_length = int(bar_length * total_completed // total_skills)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    print(f"전체 진도: {total_completed}/{total_skills} ({overall_percentage:.1f}%)")
    print(f"[{bar}] {overall_percentage:.1f}%")
    
    # 레벨 평가
    if overall_percentage >= 80:
        level = "🏆 고급자"
        message = "훌륭해요! 거의 전문가 수준이에요!"
    elif overall_percentage >= 50:
        level = "🌿 중급자"  
        message = "좋은 진전이에요! 계속 화이팅!"
    elif overall_percentage >= 20:
        level = "🌱 초급자"
        message = "좋은 시작이에요! 꾸준히 해봅시다!"
    else:
        level = "🥚 입문자"
        message = "이제 막 시작하셨네요! 천천히 해보세요!"
    
    print(f"\n🎖️  현재 레벨: {level}")
    print(f"💬 {message}")
    
    # 다음 목표 제안
    print(f"\n🎯 다음 목표:")
    if overall_percentage < 33:
        print("- [01_hello_world.py] 첫 프로그램 완성하기")
        print("- [02_calculator.py] 계산기 만들어보기")
    elif overall_percentage < 66:
        print("- 객체지향 프로그래밍 공부하기")
        print("- 실용적인 프로젝트 만들어보기")
    else:
        print("- 웹 개발 도전하기")
        print("- 포트폴리오 프로젝트 기획하기")
    
    print(f"\n📚 추천 다음 학습:")
    print("- [상세 로드맵](../../python-roadmap.md) 확인하기")
    print("- [예제 프로그램](.) 더 많이 실습하기")
    print("- [문제 해결 가이드](../../docs/troubleshooting.md) 숙지하기")

if __name__ == "__main__":
    main()
    print("\n🌟 학습 진도 체크 완료! 계속 화이팅하세요! 🚀")