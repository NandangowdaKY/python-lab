"""Display student information and calculate an academic summary."""

# Read basic student details from the keyboard.
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
course = input("Enter course: ")

# Read marks for three subjects and calculate the summary.
marks = []
for subject_number in range(1, 4):
    mark = float(input(f"Enter marks for subject {subject_number}: "))
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / len(marks)

if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent Information")
print(f"Name: {name}")
print(f"Roll number: {roll_number}")
print(f"Course: {course}")
print(f"Total marks: {total_marks:.2f}")
print(f"Average marks: {average_marks:.2f}")
print(f"Grade: {grade}")
