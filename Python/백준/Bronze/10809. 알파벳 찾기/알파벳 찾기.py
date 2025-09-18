l = list(input())
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = [-1] * len(a)

for i in range(len(a)):
    for j in l :
        if a[i] == j :
            b[i] = l.index(j)

for i in range(len(b)):
    print(b[i], end=' ')