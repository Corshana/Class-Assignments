grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
print(grades)

total_grades= sum(grades)
average_grades = total_grades / len(grades)
print(average_grades)

failed_grades == grades < 80

if failed_grades < 80:
    print(failed_grades)