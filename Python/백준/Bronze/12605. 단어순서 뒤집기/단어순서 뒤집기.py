n = int(input())
for i in range(n):
    l = input().split()
    l.reverse()
    print(f'Case #{i+1}: ',end='')
    print(*l)