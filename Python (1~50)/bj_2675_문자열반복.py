T = int(input())

for _ in range(T):
    R, S = input().split()  
    R = int(R)           # R을 정수로 변환
    for char in S:        # S의 각 문자에 대해
        print(char*R,end="")  # 해당 문자를 R번 반복
    print()               # 다음 입력을 위해 새 줄로 넘어감

# 각 출력이 같은 줄에 이어서 나타나게 하고 싶다면 end=""를 사용
