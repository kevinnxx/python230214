#DemoFIle.py

for x in range(1,6):
    print(x, "+", x, "=", x*x)

print("---오른쪽정렬---")
for x in range(1,6):
    print(x, "+", "=", str(x*x).rjust(5))

print("---0으로채우기---")
for x in range(1,6):
    print(x, "+", "=", str(x*x).zfill(5))

print("---서식 지정---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:c}".format(65))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:2f}".format(4/3))
print("{0:,}".format(15000000))

f = open("c:\\work\\demo.txt", "wt", encoding= "utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

f = open("c:\\work\\demo.txt", "rt", encoding= "utf-8")
result = f.read()
print(result)
#어디쯤 읽고 있는지
print(f.tell())
#다시 처음으로 돌아가기
f.seek(0)
print(f.tell())
lst = f.readlines()
#print(lst)
for item in lst:
    print(item, end = "")



f.close()


print("abcd"[:5])
print("test\tkkk")
