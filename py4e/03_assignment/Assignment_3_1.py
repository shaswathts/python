#print('Hey')
hour = input("Enter hours: ")
rate = input("Enter Rate: ")
hr = float(hour)
rr = float(rate)

if hr > 40 :
    #print ("Overtime")
    #print (hr, rr)
    set = 40 * rr
    ovt = (rr * 1.5 * (hr-40) )
    slr = set + ovt

else :
    #print ("Regular")
    slr = hr * rr

print("Pay:", slr)
exit()
