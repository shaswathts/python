import string 

try:
    fname = input('Enter the file name: ')
    if (len(fname) < 1): fname = 'file_1.txt'
    fhand = open(fname, "r+")
except:
    print('File cannot be opened:', fname)
    exit()

#Writing some data
fhand.write("This is line 1 in first file\n")
fhand.write("This is line 2 in first file\n")
fhand.write("This is line 3 in first file\n")
fhand.write("This is line 4 in first file\n")
fhand.write("This is line 5 in first file\n")
fhand.write("This is line 6 in first file\n")
fhand.write("This is line 7 in first file\n")
fhand.write("This is line 8 in first file\n")
fhand.write("This is line 9 in first file\n")
fhand.write("This is line 10 in first file\n")

fhand.close()

fhand_count = open(fname)

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
print("word count in file 1: ", word_count)
fhand_count.close()
