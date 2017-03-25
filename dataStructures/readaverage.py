# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    value = line.lstrip("X-DSPAM-Confidence:").strip()
    total += float(value)

# Calculate average
avg = total/count
print "Average spam confidence: %0.12f" %(avg)

