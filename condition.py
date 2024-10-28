maths=40
eng=40

if maths> eng:
    print("Maths is greater than english")
elif maths == eng:
    print("Maths and english are equal")
else:
    print("English is greater than maths")
    

    
    #write a python program that checks whether a number is positive ,negative or 0
    
number= 0

if number > 0:
    print("Number is positive")
    
elif number < 0:
    print("Number is negative")
    
else:
    print("Number is equal to 0")
    
    
    
    
#program that checks if a number is even or odd

newnum=5

if newnum%2==0:
    print("Number is even ")
else:
    print("Number is odd")
    
    
#a program that calculates the square of any given value

squarenum=int(input("Enter a number: "))

if squarenum>0:
    square=squarenum*squarenum
    print(square)
else:
    print("Can't find square of 0")
    
    
    name=string(input("Enter your name: "))