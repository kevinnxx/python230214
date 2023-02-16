#DemoRE.py
import re


result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#선택한라인 주석 ctrl + /
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())
result = re.search("\d{4}", "올해는 2023년")
print(result.group())

s = """Gee Gee Gee
너무 부끄러워

쳐다볼 수 없어
"""
c = re.compile("^.+", re.MULTILINE)
print(c.findall(s))
