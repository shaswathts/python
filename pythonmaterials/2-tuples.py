#A tuple is a package containing different values
#Read-only lists
#Enclosed in parentheses ( ( ) ) 
#Cannot be updated/change

#Syntax

person = 'Raghudathesh G P',577004,'kannada'      # tuple      #boxing = assigning many values to a single variable

name,age,hair_color = person            # un boxing un packing
print(name)
print(pincode)
print(language)


# Looping

for value in person:
    print(value)


# Nested tuples

person = 'Raghudathesh G P',('brown','black'),27
print(person[1])

# One important thing about a tuple is that it's immutable

person[0] = 'new name'
print(person)