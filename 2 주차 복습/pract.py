def calculate(a, x, y):
    a = str(a)
    if a == '+':
        x = int(x)
        y = int(y)
        return x+y
    elif a == '-':
        x = int(x)
        y = int(y)
        return x-y
    elif a == '*':
        x = int(x)
        y = int(y)
        return x*y
    elif a == '/':
        x = int(x)
        y = int(y)
        return x/y
    else:
        print("연산자 기호가 잘못 입력되었습니다.")

a,i,k = input('숫자와 연산자를 입력하세요(숫자,숫자,연산자) :').split()
while True:
    print(calculate(k,a,i))

    j = input("그만 하시겠습니까?(Y/N) :")
    if j == 'Y' or j =='y':
        break
    else:
        a,i,k = input('숫자와 연산자를 입력하세요(숫자,숫자,연산자) :').split()