
class TestClass():
    def __init__(self, p1=None,p2=None,p3=None):
        print( "init object")
        print(self.__dict__)
        if p1 != None:
            self.xx=p1
            self.printParameter(self.xx)
        if p2 != None:
            self.xy=p2
            self.printParameter(self.xy)
        if p3 != None:
            self.xz=p3
            self.printParameter(self.xz)
        print(self.__dict__)

        print()

    def printParameter(self, tmp):
        print("  parameter '%s' \t....." % tmp)

    def status(self):
        print(self.__dict__)


#aufruf

x=TestClass()
y=TestClass("eins")
z=TestClass("eins","zwei")
k=TestClass("eins","zwei","drei")
l=TestClass(2121,3354655)

z.printParameter(323232323)
print()
print(z.__dict__)   #anzeige des objects
print(k.__dict__)   #anzeige des objects

x.status()
l.status()
