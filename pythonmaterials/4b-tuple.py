# Python program to demonstrate Addition of elements in a Set 

# Creating an empty tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 

# Creating a Tuple with the use of Strings 
Tuple1 = ('INDIA', 'KARNATAKA') 
print("\nTuple with the use of String: ") 
print(Tuple1) 


# Creating a Tuple with the use of built-in function 
Tuple1 = tuple('INDIA') 
print("\nTuple with the use of function: ") 
print(Tuple1) 

# Creating a Tuple with Mixed Datatypes 
Tuple1 = (5, 'Welcome', 7, 'Goodday') 
print("\nTuple with Mixed Datatypes: ") 
print(Tuple1) 

# Creating a Tuple with nested tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'micropy') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 

# Creating a Tuple with repetition 
Tuple1 = ('INDIA',) * 3
print("\nTuple with repetition: ") 
print(Tuple1) 

#------------------------------------------------------------------
# Concatenaton of tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('red', 'white', 'green') 

Tuple3 = Tuple1 + Tuple2 

# Printing first Tuple 
print("Tuple 1: ") 
print(Tuple1) 

# Printing Second Tuple 
print("\nTuple2: ") 
print(Tuple2) 

# Printing Final Tuple 
print("\nTuples after Concatenaton: ") 
print(Tuple3)

print("\n")

#-------------------------------------------------------------

# Slicing of a Tuple with Numbers 
Tuple1 = tuple('VTU-BELAGAVI-KARNATAKA')

#finding length of a tuple
print("length of a Tuple1 is: ") 
print(len(Tuple1))
  
# Removing First element 
print("Removal of First Element: ") 
print(Tuple1[1:]) 
  
# Reversing the Tuple  
print("\nTuple after sequence of Element is reversed: ") 
print(Tuple1[::-1]) 
  
# Printing elements of a Range 
print("\nPrinting elements between Range 4-9: ") 
print(Tuple1[4:12])

#-------------------------------------------------------------

#Tuples are immutable and hence they do not allow deletion of a part of it.
#Entire tuple gets deleted by the use of del() method.

# Deleting a Tuple 
  
Tuple2 = (0, 1, 2, 3, 4) 
del Tuple2 
  
print(Tuple2)

print("\n")

#-------------------------------------------------------------



### Creating a Tuple with the use of list 
##list1 = [1, 2, 4, 5, 6] 
##print("\nTuple using List: ") 
##print(tuple(list1)) 
##
### Creating a Tuple with the use of loop 
##Tuple1 = ('INDIA') 
##n = 5
##print("\nTuple with a loop") 
##for i in range(int(n)): 
##	Tuple1 = (Tuple1,) 
##	print(Tuple1) 
