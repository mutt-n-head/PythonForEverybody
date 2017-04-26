import re
import math

def getTotal(filename):
    fh = open(filename, "r")
    runningTotal = 0

    for line in fh:
        if re.search('[0-9]+?', line):
            for newNum in re.findall('[0-9]+', line):
                runningTotal = runningTotal + int(newNum)

    return runningTotal

print getTotal("regex_sum_353704.txt")

# print "The total for big file is:", getTotal('regex_sum_42.txt')
# print "The total for the sample file is:", getTotal('small_sample.txt')
# print "The total for the assignment file is:", getTotal('regex_sum_353704.txt')


# Amount of time elapsed on Earth
# T = T0 / sqrt(1 - (v**2/c**2))
# Reverse it.
T0 = 30
multiplier = math.sqrt(1 - (math.pow(150000, 2)/math.pow(299000, 2)))
print "The multiplier is: ", multiplier
T = (T0/multiplier)
print "The time they travel is: ", T

# Playing with lists
mixList = []
mixList.append(2)
mixList.append('two')
print mixList

# Messing with dictionaries
mixDict = {}
mixDict['firstKey'] = 1
mixDict['aKey'] = 2
for item in sorted(mixDict):
    print item, "", mixDict[item]

myTuple = (2, 3, 4)
myTupleList = []
myTupleList.append(myTuple)
print myTupleList

