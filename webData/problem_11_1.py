import re

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






