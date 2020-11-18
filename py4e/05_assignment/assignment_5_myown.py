largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        ip = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = ip
    elif ip < smallest:
        smallest = ip
    elif largest is None:
        largest = ip
    elif ip > largest:
        largest = ip

print("Maximum is", largest)
print("Minimum is", smallest)
