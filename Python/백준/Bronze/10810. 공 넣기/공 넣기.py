n,m = map(int,input().split())
l = [0] * n
for _ in range(m) :
    i,j,k = map(int,input().split())
    l[i-1:j] = [k] * (j - i + 1)
print(*l)