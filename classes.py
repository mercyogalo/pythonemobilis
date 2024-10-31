class Animal:
  def __init__(self, name, number_legs):
       self.name=name
       self.number_legs=number_legs
       
  def legs(self):
        print(f"I am a {self.name} and i have {self.number_legs} legs")

my_animal1=Animal("Dog", "4")
my_animal1.legs()
  
    #print(my_animal.number_legs)
    #print(my_animal.name)

   # def move(self):
   #  print("I can walk")
      

  #objects of a class
  #OOP in python   
class Computer:
    # Special __init__ method (constructor)
    def __init__(self, ram, processor):
        self.ram = ram
        self.processor = processor
     
    def info(self):
        print(f"{self.ram} --------> {self.processor}")
      
# Creating instances of the Computer class
comp1 = Computer("8GB", "i7")
comp2 = Computer("4GB", "i3")

# Calling the info method
comp1.info()
comp2.info()

              
    

