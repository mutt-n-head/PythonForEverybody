fname = raw_input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
names = []

for line in fh:
    if line.startswith('From') and not line.startswith('From:'):
        addressLine = line.split()[1]
        print addressLine
        names.append(addressLine)


count = len(names)
print "There were", count, "lines in the file with From as the first word"
