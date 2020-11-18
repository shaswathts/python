print('Hey')
name = input("Name: ")
hour = input("Hours: ")
rate = input("Rate: ")
sc = input("Leave of absence: ")

# conversion type (string)
print ("welcome",name)
# conversion type (int - float)

try :
    hr = float(hour)
    rr = float(rate)
    la= float(sc)
except :
    print("Type only integers!")

# Two way conditional decesion

if hr > 40 :
    #print (hr, rr)
    set = 40 * rr
    ovt = (rr * 1.5 * (hr-40) )
    slr = set + ovt
    print ("Overtime pay:",slr)
    print("Overtime hours:",hr-40)

else :
    slr = hr * rr
    print ("Regular pay:",slr)

# One way conditional decesion

if la > 12:
    ela = la - 12
    print ("Extra leaves",ela)

else :
    rla = 12 - la
    print ("Remaining leave:",rla)


exit()
