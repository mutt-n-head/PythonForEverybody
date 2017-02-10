hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)

pay = 0

if h <= 0:
    pay = 0
elif h <= 40.0:
    pay = h * r
else:
    pay = (40 * r) + ((h - 40) * (r * 1.5))

print pay
