 # Student Report Card
# Beginner-level Python project for calculating total marks and percentage

print("_" * 32)
print("       STUDENT REPORT CARD")
print("_" * 32)

student_name = input("Enter student name: ").strip()
subjects = []
marks = []

for i in range(5):
    subject = input(f"Enter subject {i + 1}: ").strip()
    mark = int(input(f"Enter marks for {subject}: "))
    subjects.append(subject)
    marks.append(mark)

total_marks = sum(marks)
maximum_marks = len(marks) * 100
percentage = (total_marks / maximum_marks) * 100

print("\n" + "-" * 35)
print("Student Name:", student_name)
print("Subjects:", subjects)
print("Marks:", marks)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")

if percentage >=90:
    print("Grade:- A")
elif percentage >=70:
    print("Grade:- B")
elif percentage >= 55:
    print("Grade:-C")
else:
    print("Grade:- D")
     
if percentage >= 45:
    print("congrats 🎉 ","you will PASS")
else :
    print("FAIL","better luck next time")
    

print("_" * 32)


