a = float(input())
b = float(input())
c = float(input())
if (a+b) > c and (a+c) > b and (b+c) > a:
    if a*a == b*b+c*c or b*b == a*a+c*c or c*c == a*a+b*b:
        print('Tam giac vuong')
    elif a == b and b == c and c == a:
        print('Tam giac deu')
    else:
        print('Tam gia loai khac')
else:
    print('Khong hop le')
