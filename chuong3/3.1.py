import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
if ((a+s)>c and (a+c)>s and (s+c)>a) :
    print('Dientich=',round(s,3))
else:
    print('Khong hop le')
