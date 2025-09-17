l = []
for i in range(5) :
    a,b,c,d = map(int,input().split())
    l.append(a+b+c+d)
    
print(l.index(max(l))+1,max(l))

    
    