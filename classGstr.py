str = ""

class GString:
    def __init__(self):
        self.str = ""
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)

g =GString()
g.set("5")
g.print()
