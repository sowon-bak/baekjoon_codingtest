a,b = map(int,input().split())
seq = [i+1 for i in range(1000) for _ in range(i+1)]
print(sum(seq[a-1:b]))