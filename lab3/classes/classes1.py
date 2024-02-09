class MyClass:
    
    def getstring(self):
        self.string = input()

    def printstring(self):
        print(self.string.upper())   

p= MyClass()

p.getstring()
p.printstring()
