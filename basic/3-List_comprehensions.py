#Items separated by commas 
#Enclosed within square brackets ( [] )
#Similar to arrays in C (the items belonging to a list can be of different data type) 



import random
# Make a list of random values
our_list = []
for value in range(0,20):
    our_list.append(random.randint(0,100))

print(our_list)
print(len(our_list)

# Making a list using list comprehension

new_list = [value for value in range(0,20)]     # [ value which is being inserted into my list -- for loop ]
print(new_list) # prints the value from 0 to 19

new_list = [random.randint(0,100) for value in range(0,20)]

print(new_list)  # prints random value between0 to 100