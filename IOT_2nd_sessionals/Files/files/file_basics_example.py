#!/usr/bin/python

#This example shows very basic file operations

#Open a file in read mode

file_object = open("simple_file.txt" , "r")

print "Name of the file: ", file_object.name
print "Closed or not : ", file_object.closed
print "Opening mode : ", file_object.mode

#Close the opened file
file_object.close()

print "Closed or not : ", file_object.closed


