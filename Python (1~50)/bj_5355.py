# @ : *3 %: +5, #: -7

T = int(input())


for _ in range(T):
    case = list(map(str, input().split()))
    answer = 0
    for i in range(len(case)):
        if i == 0:
            answer += float(case[i])
        else:
            if case[i] == '#':
                answer -= 7
            elif case[i] == '%':
                answer += 5
            elif case[i] == '@':
                answer *= 3

    print("%0.2f" % answer)