#DemoStr.py

s = "abcdef"
print(s[:2])
print(s[-2:])
print(len(s))

print("c:\\work\\test.txt")
print("c:\work\test")
print(r"c:\test")


f = open("c:\\work\\data.txt", "wt", encoding="utf-8")
names = ["김길동", "홍길동", "전우치"]
for name in names:
    f.write("안녕하세요 {0}님 봄입니다...!".format(name) + "\n")
    f.write("=" * 40)
    f.write("\n")

f.close()

strA = "python is very strong"
strB = "파이썬은 강력해"
print(strA.capitalize())
print(strA.upper())
print(len(strA))
print(len(strB))
print("---알파벳과숫자로만구성---")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isalnum())
print(":::::l;;;;".isalnum())

u = "   아아아아캬아dkdk<<       spam and ham  >>>"
result = u.strip("<> dk아0캬")
print(u)
print(result)
result2 = result.replace("spam", "egg")
print(result2)
lst = result.split()
print(lst)
del lst[1]
print(" and ".join(lst))



