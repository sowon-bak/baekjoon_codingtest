n = int(input())
l = list(map(int,input().split()))
b = max(l)
t = sum(l)
a = t / b * 100 / n
print(a)