# Answer to assignment 1 for chapter 8
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print lst