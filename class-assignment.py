

class StudentInfo:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
    #instance method
    def grading(self):
     if self.marks>=80:
        print("Grade: A")
     elif self.marks>=60:
         print("Grade: B")
     elif self.marks>=40:
         print("Grade: C")
     elif self.marks>0:
        print("Grade: D")
     else:
        print("Invalid value")
    
    
StudentInfo1.name=str(input("Enter your name: "))
StudentInfo1.marks=int(input("Enter your marks:  "))
