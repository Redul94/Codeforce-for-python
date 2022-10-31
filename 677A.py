a, b = map(int, input().split())
width = 0
x = list(map(int, input().split()))
for i in range(a):
    if int(x[i]) > b:
        z = int(x[i])//b
        if x[i] % b == 0:
            width += z
        else:
            width = width+z+1
    else:
        width += 1
print(width)
