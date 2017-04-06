name = raw_input("Enter file:")
import re

if len(name) < 1 :
    name = "mbox-short.txt"

handle = open(name)
counts = {}

for line in handle:
    # if line.startswith("From "):
    #
    # Try with regular expression instead
    #
    if re.search('^From\s+', line):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1

maxword = None
maxcount = None

for email,count in counts.items():
    if maxword == None or maxcount < count:
        maxword = email
        maxcount = count

print maxword, maxcount
