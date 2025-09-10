c = list(range(1, 31))
for i in range(28):
    b = int(input())
    c.remove(b)
c.sort()
print(c[0])
print(c[1])