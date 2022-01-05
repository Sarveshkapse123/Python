def computepay(h,r) :
    if h <= 40:
       return h * r
    if h > 40:
      return (h *r) + ((h-40)*(r/2))
h = float(input('Total Hours :'))
r = float(input('Rate Per Hour :'))
P = computepay(h,r)
print('Gross Pay' ,P)
