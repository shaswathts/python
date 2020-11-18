fname = input("Enter file name: ")
count = 0
fh = open(fname)
for line in fh:
    line = line.rstrip()
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
