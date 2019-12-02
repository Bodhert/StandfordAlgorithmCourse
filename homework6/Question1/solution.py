
numbers = set()

with open('algo1-programming_prob-2sum.txt') as inputFile:
    for line in inputFile:
        num = int(line)
        numbers.add(num)

ans = 0
for i in range(-10000,10001):
    for num in numbers:
        y = i - num
        if (y != num) and ( y in numbers):
            ans += 1
            break


print(ans)
