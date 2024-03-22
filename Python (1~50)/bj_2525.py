# 오븐 시계

hh, mm = map(int, input().split())
time = int(input())

hh = hh + time//60
mm = mm + time%60

if mm >= 60:
    hh += 1
    mm -= 60
if hh >= 24:
    hh -= 24

print(hh, mm)
