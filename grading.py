

studentDetails={}


studentDetails["name"]=str(input("Enter your student name: "))
studentDetails["Reg"]=str(input("Enter your registration number: "))
studentDetails["course"]=str(input("Enter your course name: "))
studentDetails["gender"]=str(input("Enter your gender: "))





noOfSubjects=int(input("Enter the number of subjects: "))

subjects={}

total=0

for i in range(1, noOfSubjects+1):
    name=str(input(f"Enter the name of subject{i}: "))
    marks=int(input(f"Enter the marks of subject{i}: "))
    subjects[name]=marks
    total=total+marks
    
average=total/(noOfSubjects)

if average>=80:
 subjects["grade"]="A"
elif average>=60:
 subjects["grade"]="B"
elif average>=40:
   subjects["grade"]="C"
elif average>0:
    subjects["grade"]="D"
else:
    subjects["grade"]="Invalid average"

subjects["Total"]=total
subjects["average"]=int(average)

print(f"Student total marks: {subjects["Total"]}")
print(f"Student grade: {subjects["grade"]}")
