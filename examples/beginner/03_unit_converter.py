#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔄 단위 변환기 프로그램

다양한 단위를 서로 변환해주는 유용한 도구입니다!

📚 배우는 내용:
- 조건문 (if, elif, else) 사용하기
- 함수 정의하고 호출하기
- 사용자 메뉴 만들기
- 실수 계산과 반올림
"""

def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """화씨를 섭씨로 변환"""
    return (fahrenheit - 32) * 5/9

def cm_to_inch(cm):
    """센티미터를 인치로 변환"""
    return cm / 2.54

def inch_to_cm(inch):
    """인치를 센티미터로 변환"""
    return inch * 2.54

def kg_to_pound(kg):
    """킬로그램을 파운드로 변환"""
    return kg * 2.20462

def pound_to_kg(pound):
    """파운드를 킬로그램으로 변환"""
    return pound / 2.20462

# 메인 프로그램 시작
print("🔄 만능 단위 변환기")
print("=" * 30)

while True:
    print("\n📋 변환 메뉴:")
    print("1. 섭씨 → 화씨")
    print("2. 화씨 → 섭씨")
    print("3. cm → inch")
    print("4. inch → cm")
    print("5. kg → pound")
    print("6. pound → kg")
    print("7. 종료")
    
    try:
        choice = input("\n선택하세요 (1-7): ")
        
        if choice == '7':
            print("👋 단위 변환기를 이용해주셔서 감사합니다!")
            break
        
        elif choice in ['1', '2', '3', '4', '5', '6']:
            value = float(input("변환할 값을 입력하세요: "))
            
            if choice == '1':
                result = celsius_to_fahrenheit(value)
                print(f"🌡️  {value}°C = {result:.1f}°F")
                
            elif choice == '2':
                result = fahrenheit_to_celsius(value)
                print(f"🌡️  {value}°F = {result:.1f}°C")
                
            elif choice == '3':
                result = cm_to_inch(value)
                print(f"📏 {value}cm = {result:.2f}inch")
                
            elif choice == '4':
                result = inch_to_cm(value)
                print(f"📏 {value}inch = {result:.2f}cm")
                
            elif choice == '5':
                result = kg_to_pound(value)
                print(f"⚖️  {value}kg = {result:.2f}pound")
                
            elif choice == '6':
                result = pound_to_kg(value)
                print(f"⚖️  {value}pound = {result:.2f}kg")
                
        else:
            print("❌ 1-7 사이의 숫자를 입력해주세요!")
            
    except ValueError:
        print("❌ 숫자를 입력해주세요!")
    except KeyboardInterrupt:
        print("\n❌ 프로그램이 중단되었습니다. 종료합니다.")
        break

print("\n💡 학습 포인트:")
print("✅ 함수로 코드를 깔끔하게 정리했어요")
print("✅ while문으로 반복 메뉴를 만들었어요")
print("✅ 조건문으로 선택에 따라 다른 동작을 했어요")
print("✅ 에러 처리로 안전한 프로그램을 만들었어요")

# 🚀 다음 단계: 04_number_guessing.py 파일을 실행해보세요!