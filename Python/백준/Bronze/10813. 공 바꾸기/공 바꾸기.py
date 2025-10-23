n,m = map(int,input().split())
l = list(range(1,n+1))
for _ in range(m):
    a,b = map(int,input().split())
    a2 = l[a-1]
    b2 = l[b-1]
    l[a-1] = b2
    l[b-1] = a2
print(*l)