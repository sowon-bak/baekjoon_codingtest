a,b,c = map(int,input().split())
d = [a,b,c]
if a == b == c :
    print(10000+a*1000)
elif a != b and b != c and a!= c :
    print(max(d)*100)
elif a == b or b == c:
    print(b*100+1000)
else :
    print(a*100+1000)
    