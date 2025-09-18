n = int(input())
x = [[0] * 100 for _ in range(100)]
c = 0

for k in range(n):
    a, b = map(int, input().split())
    for l in range(10):
        for i in range(10):
            x[a + l][b + i] = 1

for i in range(100):
    for j in range(100):
        if x[i][j] == 1:
            c += 1

print(c)

    
    
