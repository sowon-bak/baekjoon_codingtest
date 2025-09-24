n = int(input())
for _ in range(n):
    w = input()
    g = w.count('g') + w.count('G')
    b = w.count('b') + w.count('B')
    if g > b :
        print(f'{w} is GOOD')
    elif g < b :
        print(f'{w} is A BADDY')
    else :
        print(f'{w} is NEUTRAL')
        