

class StudentInfo:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        
    #instance method
    def grading(self):
     if self.marks[average]>=80:
        print(f"Grade: A")
     elif self.marks[average]>=60:
         print("Grade: B")
     elif self.marks[average]>=40:
         print("Grade: C")
     elif self.marks[average]>0:
        print("Grade: D")
     else:
        print("Invalid value")
    
    
name=str(input("Enter your name: "))
noOfSubjects=int(input("Enter the number of subjects: "))
marks={}


total=0

for i in range(1, noOfSubjects+1):
    marks[subjectName]=str(input(f"Enter the name of subject{i}: "))
    marks[subjectMark]=int(input(f"Enter the marks of subject{i}: "))
    total=total+subjectMark
    
average=total/(noOfSubjects)
marks[average]=average


StudentInfo1=StudentInfo(name,marks)
StudentInfo1.grading()