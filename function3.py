#function3.py


def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자 방식
def connectURI(server, port):
    strURI = "http://" + server + ":" + port
    return strURI
    print("---------")
    print("http://", server, port)

#호출
print(connectURI("credu.com", "80"))
print(connectURI(port = "8080", server= "credu.com"))



#가변인자(가변적인 상황처리)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM", "EGG" ))
print(union("HAM", "EGG", "SPAM"))

#정의되지 않은 인자 처리
def userURIBuilder(server, port, **user):
    strURI = "https://" + server + ":" + port + "/?"  
    for key in user.keys():
        strURI += key + "=" + user[key] + "&"
    return strURI

#호출
print(userURIBuilder("credu.com", "80", id= "kim", password="1234"))
print(userURIBuilder("credu.com", "80", id= "kim", password="1234", 
name = "mike"))
print(userURIBuilder("credu.com", "80"))

#람다함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())
