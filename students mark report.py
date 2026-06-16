def assign_grade(marks):
    if marks >= 80 and marks <= 100:
        return "A"
    elif marks >=60 and marks < 80:
        return "B"
    elif marks >= 40 and marks < 60:
        return "C"
    else:
        return "F"
students = []
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks (out of 100) for {name}: "))
    grade = assign_grade(marks)
    students.append((name, marks, grade))
total_marks = sum(marks for _, marks, _ in students)
average_marks = total_marks / len(students)
report_lines = []
report_lines.append("===== STUDENT MARKS REPORT =====")
report_lines.append("Name        Marks   Grade")
report_lines.append("----------------------------")

for name, marks, grade in students:
    report_lines.append(f"{name:<10}   {marks:<5}   {grade}")

report_lines.append("----------------------------")
report_lines.append(f"Class Average: {average_marks:.1f}")
report_lines.append("Report saved to marks_report.txt")

for line in report_lines:
    print(line)

with open("marks_report.txt", "w") as file:
    for line in report_lines:
        file.write(line + "\n")
