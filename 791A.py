a,b= map(int,(input().split()))
count=0
while True:
     if a >b:
        print(count)
        break
     else:
        a=a*3
        b=b*2
        count=count+1
