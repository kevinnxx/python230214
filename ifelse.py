# ifelse.py
score = int(input("score: "))

if 90 <= score < 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "D"
    
print("등급은: ", grade)
