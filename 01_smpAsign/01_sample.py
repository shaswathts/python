# Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable.

list = []
x = 10
y = 20
print("value of x = ",x)
print("value of y = ",y) 
list.append(x)
list.append(y)
print("After exchanging")
list[0],list[1] = list[1],list[0] 
x = list[0]
y = list[1]
print("value of x = ",x)
print("value of y = ",y)


