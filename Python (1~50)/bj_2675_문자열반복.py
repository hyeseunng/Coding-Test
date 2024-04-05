T = int(input())

# for _ in range(len(T)):  # 반복횟수 # 문자열
#     R, S = map(input().split())
#     result = []
#     for i in range(len(S)):
#         result = S[i]*R

for j in range(T):
    i, S = input().split()
    for k in S:
        print(k*int(i),end="")
    print()