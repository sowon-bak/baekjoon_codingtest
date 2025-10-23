l = []
for _ in range(10):
    a = int(input())
    b = a%42
    if b in l:
        pass
    else :
        l.append(b)
print(len(l))