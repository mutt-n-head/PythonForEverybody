# Assignment for week 4
hrs = raw_input('Enter hours:')
rate = raw_input('Enter rate:')

# All raw input taken in as String type, needs conversion.
hrs = int(hrs)
rate = float(rate)

print "%1.2f" % (hrs * rate)
