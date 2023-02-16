#try1.py

def divide(a,b):
    return a/b 

try:
    result = divide(5,2)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
except TypeError:
    print("숫자형식이여야합니다")
else:
    print("결과: {0}".format(result))
finally:
    print("이중체크")

