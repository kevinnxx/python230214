#class1.py
#클래스정의
class Person:
    num_person = 0
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print("my name s {0}".format(self.name))

#인스턴트 생성
#p1 = Person()
#메서드 호출
#p1.print()

#인스턴스 생성
p1 = Person()
p2 = Person()
print("인스턴스 갯수:{0}".format(Person.num_person))
p1.age = 3
print(p1.age)
print(p2.age)
#p1.name = "전우치"
#메서드호출
p1.print()
#p2.print()

#동적으로 형식이 변경
Person.title = "New Title"
print(p1.title)
print(p2.title)
print(Person.title)

