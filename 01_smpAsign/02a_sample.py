# Python Program to Print all Numbers in a Range Divisible by a Given Number. 
# [ if range is from 1 to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]

print("Enter a Range of number")
fh = int(input("Range: "))
fp = int(input("Divisiblity of: "))
for i in range(1, fh+1):
    Number = i
    answer = Number%fp
    if answer == 0:
        print("Numbers which were divisible: ",i)
