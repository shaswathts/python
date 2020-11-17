# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Creating a Dictionary with Integer Keys 
Dict = {1: 'High', 2: 'Low', 3: 'medium'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

# Creating a Dictionary with Mixed keys 
Dict = {'Name': 'Good', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

# Creating a Dictionary with dict() method 
Dict = dict({1: 'Happy', 2: 'Go', 3:'Lucky'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict)

#----------------------------------------------------------------

# Creating and accessig a Nested Dictionary 

Dict = {1: 'Banglore', 2: 'For', 
		3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Bangaluru'}} 

print("\n Accessing elements in nested dict: ")
print(Dict[1]) 
print(Dict[3]['A']) 
print("\n")
#----------------------------------------------------------------

#Adding elements to a Dictionary

# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Adding elements one at a time 
Dict[0] = 'Good'
Dict[2] = 'Better'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Adding set of values to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict)
print("\n")
#----------------------------------------------------------------

# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
		'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
		'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 

# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 

# Deleting a Key from Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 

# Deleting a Key using pop() 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 

# Deleting a Key using popitem() last key-value are deleted
Dict.popitem() 
print("\nPops first element: ") 
print(Dict) 

# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 

print("\n")

#------------------------------------------------------------------
