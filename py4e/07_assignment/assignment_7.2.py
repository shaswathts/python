# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    #print(line)
    #print(line.find(':'))
    #detect = line[19:]
    delspc = line[19:].lstrip()
    convt = float(delspc)
    total = total + convt
    avg = total/count
    #print(convt)

print("Average spam confidence:",avg)
#print(count)
#print(total)
#print(avg)
