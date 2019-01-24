class PartyAnimal():
    x = 1

    def add_one(self):
        self.x += 1

    def some_function(self):
        print('some function in PARTY animal')


class OriginalAnimal:
    y = 44
    originalAnimalStr = 'original animal'

    def some_function(self):
        print('some function in ORIGINAL animal')


class AnotherAnimal(OriginalAnimal, PartyAnimal):
    someStr = ""

    def __init__(self, beginstr):
        self.someStr = beginstr

    def create_string(self, instr):
        self.someStr = self.someStr + " " + instr

    def some_function(self):
        PartyAnimal.some_function(self)

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
print(aa.y)
aa.some_function()

# Neat trick for printing fancy wise
# Note the spread operation on the data dictionary object

data = {
    'hometown': 'Baltimore',
    'fname': 'Joe',
    'lname': 'Sixpack',
    'age': 23,
    'random': 'frankp'
}

some_str = ['one', 'two', 'three', 'four', 'five']

print(data)
print('Resuts are {fname} and {lname} who is {age} years old'.format(**data))


def takes_some_args(fname, lname, age, hometown, random):
    print('{} {} who is {} and originally from {}'.format(fname, lname, age, hometown))

    if random:
        print('There was another which was {}'.format(random))


takes_some_args(*some_str)
# If you pass dictionary the names must match.  If they do not, then unexpected keyword argument error
takes_some_args(**data)

