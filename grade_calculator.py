grade_percentage = int(input("Enter your grade percentage: "))
grade_bal = grade_percentage % 10
grade_sign = ""
grade = ""

if grade_bal >= 7:
    grade_sign = "+"
elif grade_bal < 3:
    grade_sign = "-"


if grade_percentage >= 90:
    grade = "A"
elif grade_percentage >= 80:
    grade = "B"
elif grade_percentage >= 70:
    grade = "C"
elif grade_percentage >= 60:
    grade = "D"
else:
    grade = "F"

if grade_percentage >= 97 or grade_percentage < 60:
    grade_sign = ""

print(f"Your grade is: {grade}{grade_sign}")