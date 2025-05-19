students = [
    {'id': '1000', 'name': 'Jane Smith', 'age': 20},
    {'id': '1001', 'name': 'John White', 'age': 16},
    {'id': '1002', 'name': 'Alex Brown', 'age': 19},
    {'id': '1003', 'name': 'Mary Johns', 'age': 17}
]

print('1. sort the students in a ascending order of age:')
sorted_students = sorted(students, key=lambda x: x['age'])
for sorted_by_age in sorted_students:
    print(sorted_by_age)

print('2. sort the students by surname')
sorted_students = sorted(students, key=lambda x: x['name'].split()[1])
for sorted_by_surname in sorted_students:
    print(sorted_by_surname)