#print('hey')
def computepay():
    if hr > 40 :
        #print ("Overtime")
        #print (hr, rr)
        set = 40 * rr
        ovt = (rr * 1.5 * (hr-40) )
        slr = set + ovt
        return slr
    else :
        #print ("Regular")
        slr = hr * rr
        return slr

hour = input("Enter hours: ")
rate = input("Enter Rate: ")
hr = float(hour)
rr = float(rate)
p = computepay()
print ("Pay",p)

# or use this code

def computepay(hr, rr):
    if hr > 40 :
        set = 40 * rr
        ovt = (rr * 1.5 * (hr-40) )
        slr = set + ovt
        return slr
    else :
        slr = hr * rr
        return slr

hour = input("Enter hours: ")
rate = input("Enter Rate: ")
hr = float(hour)
rr = float(rate)
p = computepay(hr, rr)
print("Pay",p)
