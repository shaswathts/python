# Python code to demonstrate working of startswith() and endswith() 
str = "apple"
str1 = "appleorangeraspberrypeachapple"

# using startswith() to find if str starts with str1 
if str1.startswith(str): 
		print ("str1 begins with : " + str) 
else : print ("str1 does not begin with : "+ str) 

# using endswith() to find if str ends with str1 
if str1.endswith(str): 
	print ("str1 ends with : " + str) 
else : print ("str1 does not end with : " + str)


print ("\n")

#-------------------------------------------------------------------

# Python code to demonstrate working of isupper() and islower() 
str = "DavangereShivamogga"
str1 = "butterdosa"

# checking if all characters in str are upper cased 
if str.isupper() : 
	print ("All characters in str are upper cased") 
else : print ("All characters in str are not upper cased") 

# checking if all characters in str1 are lower cased 
if str1.islower() : 
	print ("All characters in str1 are lower cased") 
else : print ("All characters in str1 are not lower cased") 

print ("\n")

#-------------------------------------------------------------------

# Python code to demonstrate working of upper(), lower(), swapcase() and title() 
str = "Buliding Smart ThinGS By lEVEraging IOt TeChNoLoGy USING nodemcU RASPBErry pi"



# Coverting string into its lower case 
str1 = str.lower(); 
print (" The lower case converted string is : " + str1) 
print ("\n")
# Coverting string into its upper case 
str2 = str.upper(); 
print (" The upper case converted string is : " + str2) 
print ("\n")
# Coverting string into its swapped case 
str3 = str.swapcase(); 
print (" The swap case converted string is : " + str3) 
print ("\n")
# Coverting string into its title case 
str4 = str.title(); 
print (" The title case converted string is : " + str4)

print ("\n")

# Determining type of a variable 
print (type(str))
str2 = 1
print (type(str2))
#------------------------------------------------------------------
