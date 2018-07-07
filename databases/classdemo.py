class PartyAnimal():
    x = 0

    def add_one(self):
        self.x += 1


class AnotherAnimal(PartyAnimal):
    someStr = ""

    def __init__(self, beginstr):
        self.someStr = beginstr

    def create_string(self, instr):
        self.someStr = self.someStr + " " + instr

    def __del__(self):
        print("This is AnotherAnimal's destructor")


pa = PartyAnimal()
pa.add_one()
print(pa.x)

aa = AnotherAnimal('Starter String')
aa.add_one()
aa.add_one()
aa.create_string('... and yet more')
print(aa.someStr)
print(aa.x)

# Neat trick for printing fancy wise
# Note the spread operation on the data dictionary object

data = {
    'fname': 'Joe',
    'lname': 'Sixpack',
    'age': 23
}

print('Resuts are {fname} and {lname} who is {age} years old'.format(**data))
