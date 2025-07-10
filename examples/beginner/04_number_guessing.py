#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎲 숫자 맞추기 게임

컴퓨터가 생각한 숫자를 맞춰보는 재미있는 게임입니다!

📚 배우는 내용:
- random 모듈 사용하기
- while문으로 게임 루프 만들기
- 조건문으로 게임 로직 구성하기
- try-except로 입력 에러 처리하기
- 변수로 게임 상태 관리하기
"""

import random

print("🎲 숫자 맞추기 게임")
print("=" * 30)
print("컴퓨터가 1부터 100까지 숫자 중 하나를 생각했어요!")
print("몇 번 만에 맞출 수 있을까요? 🤔")

# 게임 설정
secret_number = random.randint(1, 100)  # 1부터 100까지 랜덤 숫자
attempts = 0  # 시도 횟수
max_attempts = 7  # 최대 시도 횟수
game_over = False  # 게임 종료 여부

print(f"\n🎯 규칙: {max_attempts}번의 기회가 있어요!")
print("💡 힌트: 각 시도마다 '더 큰 수' 또는 '더 작은 수' 힌트를 드려요!")

# 게임 루프 시작
while not game_over and attempts < max_attempts:
    try:
        # 사용자 입력 받기
        remaining = max_attempts - attempts
        print(f"\n🔢 숫자를 입력하세요 (남은 기회: {remaining}번)")
        
        guess = int(input("당신의 추측: "))
        
        # 입력 범위 확인
        if guess < 1 or guess > 100:
            print("❌ 1부터 100까지의 숫자를 입력해주세요!")
            continue
            
        attempts += 1
        
        # 정답 확인
        if guess == secret_number:
            print("🎉 대박! 정답입니다!")
            print(f"👏 축하해요! {attempts}번 만에 맞췄네요!")
            
            # 실력 평가
            if attempts <= 3:
                print("🏆 천재! 정말 대단해요!")
            elif attempts <= 5:
                print("😊 훌륭해요! 센스가 좋으시네요!")
            else:
                print("😌 잘하셨어요! 꾸준히 하면 더 잘하실 거예요!")
                
            game_over = True
            
        elif guess < secret_number:
            print("📈 틀렸어요! 더 큰 숫자를 생각해보세요!")
            print(f"💭 힌트: {guess}보다 큰 수예요")
            
        else:  # guess > secret_number
            print("📉 틀렸어요! 더 작은 숫자를 생각해보세요!")
            print(f"💭 힌트: {guess}보다 작은 수예요")
            
        # 남은 기회 확인
        remaining = max_attempts - attempts
        if remaining > 0 and not game_over:
            print(f"⏰ {remaining}번의 기회가 남았어요! 화이팅!")
            
    except ValueError:
        print("❌ 숫자만 입력해주세요! (예: 50)")
    except KeyboardInterrupt:
        print("\n❌ 게임이 중단되었습니다! 다음에 다시 도전해주세요!")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 예상치 못한 오류가 발생했습니다: {e}")
        print("🚨 프로그램을 종료합니다. 문제가 지속되면 개발자에게 문의하세요.")
        sys.exit(1)

# 게임 종료 처리
if not game_over:
    print(f"\n😅 아쉽게도 기회를 다 쓰셨네요!")
    print(f"🔍 정답은 {secret_number}였습니다.")
    print("💪 다시 도전해보세요! 연습하면 더 잘하실 거예요!")

print(f"\n📊 게임 통계:")
print(f"🎯 시도 횟수: {attempts}번")
print(f"🎲 정답: {secret_number}")

# 다시 게임하기 제안
print("\n🔄 또 다른 게임을 해보고 싶다면 프로그램을 다시 실행하세요!")

print("\n💡 학습 포인트:")
print("✅ random.randint()로 랜덤 숫자 생성")
print("✅ while문으로 게임 반복")
print("✅ 조건문으로 게임 로직 구현")
print("✅ 변수로 게임 상태 관리")
print("✅ 사용자 친화적인 메시지와 이모지")

# 🚀 다음 단계: 05_grade_calculator.py 파일을 실행해보세요!