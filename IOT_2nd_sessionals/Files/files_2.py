import string

fhand = open("file_1.txt", "r")
fhand1 = open("file_2.txt", "w")
fdata = fhand.readlines()
for line in reversed(fdata):
    print(line)
    fhand1.write(line)
fhand.close()
fhand1.close()

fhand_count = open("file_2.txt")

counts = dict()
for line in fhand_count:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
word_count = 0
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
    word_count += val

lst.sort(reverse=True)
print("word count in file 2: ", word_count)
fhand_count.close()

