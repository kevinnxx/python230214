#function2.py

print('불변')
a = 1.2
print(id(a))
a=2.3
print(id(a))

print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

x = 5
def func2(a):
    return a+x

#호출
print(func2)

#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM", "SPAM"))

#전역변수(불변)에 읽기, 쓰기

g = 1 
def testScope(a):
    global g
    g = 2
    return a+g

#호출
print(testScope(1))
print("전역변수 g: ", g)

#가변형식
wordlist = ["J", "A", "M"]
for i in []:
    wordlist[0] = "H"
    print("----")
    print(wordlist)

#호츨
#change(wordlist)
print(wordlist)