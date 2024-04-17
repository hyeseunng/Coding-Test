sum = 0

for _ in range(5):
    score = int(input())
    if score < 40:
        sum += 40
    else:
        sum += score

avg = int(sum/5)
print(avg)
