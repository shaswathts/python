#!/usr/bin/python

#This example shows basic write operation

#Open a file in write mode (text)

file_object = open("write_ex.txt", "r+")
print ("File: " , file_object.name, " opened successfully.\n")

#Writing some data
file_object.write("This is a write example. ")

#Writing some more data
file_object.write("This data will come on the same line.")

#Writing on a new line
file_object.write("\nWriting on a new line with a new line character.")
print ("\nContents written to the file.\n")

#Pointing the pointer to the 0th location 

file_object.seek(0)

#Reading contents of the file

full_data = file_object.read()
print ("\nFull File Content: \n", full_data)

#Pointing the pointer to the 0th location 

file_object.seek(0)

#Reading contents of the file line wise

data = file_object.readline()
print ("\nLine in the file: \n", data)

#Closing the file
file_object.close()
