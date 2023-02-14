#그냥그저그런파일.py


t = 20* 10
for i in list(range(0,201,20)):
    while t > 0:
        t -= 1
        if t == i:
            print(t)