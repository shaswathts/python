# Python Program to Check Whether a Number is Positive or Negative

print("Enter a number to check if its Positive or Negative")
fh = input("Enter a Number: ")
# The input() command will take a string and we have to convert to int in order to 
# perform calculation's with it
x = int(fh)
if x == 0 :
    print("The number you entered is Zero")
elif x < 0 :
    print("The number you entered is Negative")
elif x > 0 :
    print("The number you entered is Positive")    
exit()