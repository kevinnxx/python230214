#DemoSetTuple.py
tp = (1,2,3)
print( len(tp) )
print( tp[0] )

#함수정의
def calc(a, b):
    return a+b, a*b

#함수호출
result = calc(3, 4)
print(result[0])
print(result[1])

print("id:%s, name:%s" % ("kim", "김승두"))

print("-----set-----")
a = {1,2,3,4}
b = {3,4,4,5}
print(a)
print(b)
print( a.intersection(b) )
print( a.difference(b) )
print(a|b)
print(a&b)
print(a-b)


print("-----변환-----")
b = set((1,2,3))
print( type(b) )
print( b )
c = list(b)
c.append(4)
print(c)


color = {"apple":"red", "banana":"yello"}
print( len(color) )
print( color["apple"] )
del color["apple"]
print( color )
