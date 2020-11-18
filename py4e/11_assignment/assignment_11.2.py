import re
sum = 0
x = open("regex_sum_696288.txt")
for line in x:
    line = line.rstrip()
    q = line.split()
    #print("line:",line)
    for i in q:
        y = re.findall('[0-9]+',i)
        for e in range(0, len(y)):
            y[e] = int(y[e])
            sum = y[e] + sum
print("Number:",sum)
