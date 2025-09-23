n = int(input())
a = list(map(int,input().split()))
v = int(input())
c = 0
for i in a:
    if v == i :
        c += 1
print(c)        
