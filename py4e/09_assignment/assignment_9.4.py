count = dict()
fh = open("mbox-short.txt")
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    word = words[1]
    count[word] = count.get(word,0) + 1

bigcount = None
bigword = None
for key,value in count.items():
    if bigcount == None:
        bigcount = value
    elif value > bigcount:
        bigcount = value
        bigword = word
print(bigword,bigcount)
