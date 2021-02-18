#!/usr/bin/python

#This example shows basic read operation

#Open a file in read mode (text)

file_object = open("simple_file.txt", "r")

#Reading contents of the file

full_data = file_object.read()
print "\nFull File Content: \n", full_data

#Pointing the pointer to the 0th location as the pointer reached EOF during file_object.read()

file_object.seek(0)

#Reading content count wise

data = file_object.read(10)
print "\nFirst 10 Charecters: \n", data

#Pointing the pointer to the 2nd location
file_object.seek(2)


#Confirming the location of the pointer

print "\nPointer at: ", file_object.tell()

#Reading data at 2nd location

print "\n5th Location: " , file_object.read(1)

#Checking the location of the pointer

print "\nPointer at: ", file_object.tell()

#Closing the file

file_object.close()
