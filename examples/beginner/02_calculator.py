#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧮 간단한 계산기 프로그램

사용자로부터 두 숫자를 입력받아서 사칙연산을 수행하는 프로그램입니다.

📚 배우는 내용:
- input() 함수로 사용자 입력 받기
- int(), float() 함수로 데이터 타입 변환
- 사칙연산 (+, -, *, /) 사용하기
- f-string으로 결과 예쁘게 출력하기
- try-except로 에러 처리하기
"""

print("🧮 간단한 계산기에 오신 것을 환영합니다!")
print("=" * 40)

try:
    # 사용자로부터 숫자 입력받기
    print("두 개의 숫자를 입력해주세요:")
    num1 = float(input("첫 번째 숫자: "))
    num2 = float(input("두 번째 숫자: "))
    
    print("\n📊 계산 결과:")
    print("-" * 30)
    
    # 사칙연산 수행하기
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # 결과 출력하기
    print(f"➕ {num1} + {num2} = {addition}")
    print(f"➖ {num1} - {num2} = {subtraction}")
    print(f"✖️  {num1} × {num2} = {multiplication}")
    
    # 나눗셈은 0으로 나누기 에러를 조심해야 해요!
    if num2 != 0:
        division = num1 / num2
        print(f"➗ {num1} ÷ {num2} = {division:.2f}")  # 소수점 2자리까지
    else:
        print("➗ 0으로 나눌 수 없습니다! 😅")
    
    print("\n🎉 계산 완료!")
    
except ValueError:
    print("❌ 오류: 숫자만 입력해주세요!")
except Exception as e:
    print(f"❌ 예상치 못한 오류가 발생했습니다: {e}")

print("\n💡 도전 과제:")
print("- 나머지 연산(%)도 추가해보세요!")
print("- 제곱 연산(**)도 추가해보세요!")
print("- 더 많은 숫자로 계산해보세요!")

# 🚀 다음 단계: 03_unit_converter.py 파일을 실행해보세요!