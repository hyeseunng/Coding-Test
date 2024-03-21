# (세 자리 수) × (세 자리 수) 곱셈

# items = input().split(',')  # 쉼표로 구분된 입력을 리스트로 변환

a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b//10)%10))
print(a*((b//100)%10))
print(a*b)