#Function definition called simple_print
def simple_print(value):
	print "\nThis is simple_print function.\nDoes not return any value."
	print value
	return

#Fuction denitition for calculating sum	
def sum(a, b):
	print "\nThis function calculates the sum and returns it."
	return ( a + b )

#Function definition for multiplication. Also shows that one function can call another.	
def multiply(a, b):
	print "\nThis is multiply funtion. Calling simple_print to print the product. This function does not return any values.\n"
	simple_print( a * b ) 
	return 

#Optional main function, need not be present always.


if __name__ == "__main__":
	simple_print("Hello World!")
	x = sum( 5 , 88 )
	print "The Sum of 5 & 88 is: " , x
	multiply( 4 , 6 )
	

