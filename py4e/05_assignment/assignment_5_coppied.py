largest = -1
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        numb = float(num)
    except:
        print ("Invalid input")
    if smallest is None:
        smallest = numb
    if numb > largest :
        largest = numb
    elif numb < smallest :
        smallest = numb

def done(largest,smallest):
    print ("Maximum is", int(largest))
    print ("Minimum is", int(smallest))

done(largest,smallest)
