class PartyAnimal():
    x = 0

    def addOne(self):
        self.x += 1


class AnotherAnimal(PartyAnimal):
    someStr = ""

    def __init__(self, beginstr):
        self.someStr = beginstr
    def createString(self, instr):
        self.someStr = self.someStr + " " + instr
    def __del__(self):
        print "This is AnotherAnimal's destructor"


pa = PartyAnimal()
pa.addOne()
print pa.x

aa = AnotherAnimal('Starter String')
aa.addOne()
aa.addOne()
aa.createString('... and yet more')
print aa.someStr
print aa.x


