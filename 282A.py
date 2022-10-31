n = int(input())
x = 0
for _ in range(0,n):
    y = input()
    if y[0] == '+' or y[-1] == '+':
        x += 1
    else:
        x -= 1
print(x)
