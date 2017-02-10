score = raw_input("Enter Score: ")

try:
    s = float(score)
    if s < 0.0 or s > 1.0:
        print 'Please enter a number between 0.0 and 1.0'
    elif s < .6:
        print 'F'
    elif s < .7:
        print 'D'
    elif s < .8:
        print 'C'
    elif s < .9:
        print 'B'
    else:
        print 'A'

except:
    print 'Please enter a number next time'
