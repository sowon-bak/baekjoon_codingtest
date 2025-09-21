n = int(input())
if n%4 == 0 :
    a = n // 4
else :
    a = ( n // 4 ) + 1
print('long ' * a + 'int')