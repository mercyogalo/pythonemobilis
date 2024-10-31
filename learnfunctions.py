#def avr(number1: int, number2: int, number3: int):
  #  return (number1+ number2 + number3) / 3

#average=avr(45,76,84)
#print(average)


#def calculator(num1 : int , num2 : int):
  #  print(f"Perimeter : {2*(num1+ num2)}")
  #  print(f"Area: {num1 * num2}")
    
#calculator(2,5)

#def people(name="Joseph", age=10 ):
 
# return print(f"Hello, i am {name.upper()} and i'm {age} years old") 
  
  
#people("Mercy", 20)


temperature=0


def kelvin(num: int):
    kelvintemperature=num + 273.15
    
    print(f"Temperature in kelvin is {kelvintemperature}")
    
    
def fahrenheit(num: int):
  fahrenheittemperature=num*(9/5) + 32
  
  print(f"Temperature in fahrenheit is { fahrenheittemperature}")
    
    

def celcius():
  global temperature
  
temperature=int(input("Enter the temperature: "))
conversion=str(input("Enter the conversion name: "))
  

if conversion.lower()=="kelvin":
      kelvin(temperature)
elif conversion.lower=="fahrenheit":
     fahrenheit(temperature)
else:
    print("Enter a valid conversion either kelvin or fahrenheit")






  
  

 



celcius()

