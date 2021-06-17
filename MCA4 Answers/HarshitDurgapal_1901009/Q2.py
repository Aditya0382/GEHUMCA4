def test(dictt, key, value):
    if any(sub[key] == value for sub in dictt):
        return True
    return False
employees = [
    {'employee_id': 10110, 'name': 'James Parkes', 'Dept': 'IT'},
    {'employee_id': 10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'},
    {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
    {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'},
    {'employee_id': 10115, 'name': 'Jeff Simson', 'Dept': 'HR'}
]
print("Original dictionary:")
print(employees)
print("Check if a specific Key and a value exist in the said dictionary:")
print(test(employees, 'employee_id', 10110))
print(test(employees, 'name', 'Brian Adam'))
print(test(employees, 'Dept', 'HR'))
print(test(employees, 'Dept', 'CEO'))
print(test(employees, 'name', 'Harshit Durgapal'))
print(test(employees, 'employee_id', 10116))
