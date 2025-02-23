#numbers (1)

def function_arguments(num, char):
    return " The number is {} and the character is '{}' ".format(num, char)

result = function_arguments(145, 'o')
print(result)

#numbers (2)

radius=84
pi=3.14
area=pi*(radius**2)
print("area of the pond is : ",area,"square meter")
print("total water in the pond is : ",round((1.4)*area),"litres")

#numbers (3)

distance=490
time=7*60 #converting time in seconds
speed=distance//time
print(speed,"m/s")
