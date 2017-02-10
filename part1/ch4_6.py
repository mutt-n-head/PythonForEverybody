def computepay(h, r):
    pay = 0.0

    if h < 0:
        pay = 0.0
    elif h <= 40.0:
        pay = h * r
    else:
        pay = (40 * r) + ((h - 40) * (r * 1.5))

    return pay


hrs = raw_input("Enter Hours:")
hrs = float(hrs)
rate = raw_input("Enter Rate:")
rate = float(rate)

p = computepay(hrs, rate)

print p
