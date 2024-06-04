students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

students.extend(grades)
students.extend(activities)
print(students)

for student, grade, activity in zip(students, grades, activities):
    if grade < 80:
        print(f"{student}, {grade}, {activity}")

students_approved = [student for student, grade in zip(students, grades) if grade >= 80]
print (students_approved)

