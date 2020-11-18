hf = open("mbox-short.txt")

#hcount = dict()
#hlst = ()

#for line in hf:
#    words = line.split()
#    if len(words) == 0 : continue
#    if words[0] == 'From': continue
#    print("found words",words)
#    hr = words[0].split(':')
#    hcount[hr[0]] = hcount.get(hr[0], 0) + 1

#for k,v in hcount.items():
#    hlst.append((k,v))
#hlst.sort()
#for k,v in hlst:
#    print(k,v)

hcount = dict()                                     #create empty dictionary
hlst = []                                           #create empty list

for line in hf:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       #Select lines with 'From'
        hr = words[5].split(':')                    #Select hour (5th index) and split string with colon
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1    #increase count for each hour
    else:
        continue

for k,v in hcount.items():                           #k = hour, v = count
    hlst.append((k,v))                               #append tuples to list

hlst.sort()                                         #sort list by hour
for k,v in hlst:                                    #loop through list of tuples
    print (k,v)                                       #print counts sorted by hour
