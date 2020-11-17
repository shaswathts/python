#A tuple is a package containing different values
#Read-only lists
#Enclosed in parentheses ( ( ) ) 
#Cannot be updated/change

#Syntax

person = ('Raghudathesh G P',577004,'kannada')      # tuple      #boxing = assigning many values to a single variable

name,pincode,language = person            # un boxing un packing
print(name)
print(pincode)
print(language)


# Looping

for value in person:
    print(value)


# Nested tuples

person = ('Raghudathesh G P',('brown','black'),27)
print(person[1])

# One important thing about a tuple is that it's immutable

x = person[2]
print(x)

# This 2 line code bellow is to prove that a tuple can not be modified hence you get the 
# Error msg saying that 
# person[0] = 'new name'
# TypeError: 'tuple' object does not support item assignment

person[0] = 'new name'
print(person)