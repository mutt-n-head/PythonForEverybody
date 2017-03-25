fname = raw_input("Enter file name:")
try:
    fhandle = open(fname, "r")
except:
    print("Error opening file named:  %s", fname)

for line in fhandle:
    print(line.rstrip().upper())

