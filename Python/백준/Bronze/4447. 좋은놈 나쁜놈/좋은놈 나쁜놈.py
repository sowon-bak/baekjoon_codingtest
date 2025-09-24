n = int(input())
for _ in range(n):
    w = input()
    g = w.count('g')
    G = w.count('G')
    b = w.count('b')
    B = w.count('B')
    gg = g + G
    bb = b + B
    if gg > bb :
        print(f'{w} is GOOD')
    elif gg < bb :
        print(f'{w} is A BADDY')
    else :
        print(f'{w} is NEUTRAL')
        