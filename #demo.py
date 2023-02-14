#demo.py


colors = ["red", "green", "blue"]
print( colors )
colors.append("white")
print( colors )
colors.append("black")
print( colors )
colors.insert(1, "yellow")
colors += ["red"]
print(colors.index("red"))
print(colors.count("red"))
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
colors.remove("red")
print( colors )
colors.extend(["red", "pink", "white"] )
print( colors )
colors.reverse()
print( colors )