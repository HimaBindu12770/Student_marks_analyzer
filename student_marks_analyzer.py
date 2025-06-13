# student_marks_analyzer.py

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

# Main program
student_name = input("Enter student name: ")
marks = []

# Getting 5 subject marks
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)

print("\n----- Student Report -----")
print(f"Name       : {student_name}")
print(f"Marks      : {marks}")
print(f"Total      : {total}")
print(f"Average    : {average:.2f}")
print(f"Grade      : {grade}")
print("--------------------------")
