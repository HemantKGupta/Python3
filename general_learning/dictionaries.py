students = {"first":1, "second":2, "third":3}
print(students)
del students["second"]
print(students)
students.clear()
print(students)
del students
students = {"first":1, "second":2, "third":3}
print(len(students))
print(students.keys())
students2 = {"fourth":4, "fifth":5}
students.update(students2)
print(students)
