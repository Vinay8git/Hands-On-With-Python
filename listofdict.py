list1 = [{'name': "test1", 'rollno': 1}, {'name': "test2", 'rollno': 2}, {'name': "test3", 'rollno': 3}]
print(list1)
print("enter 1 to add")
print("enter 2 to search")
print("enter 3 to edit")
print("enter 4 to delete")
ch = int(input("Enter choice"))
if ch == 1:
    name = input("Enter name")
    rollno = int(input("Enter rollno"))
    list1.append({'name': name, 'rollno': rollno})
    print(list1)
elif ch == 2:
    rollno = int(input("Enter rollno"))
    name = input("Enter name to be updated corresponding to rollno")
    for record in list1:
        if record["rollno"] == rollno:
            print("record found successfully")
            break
        else:
            print("record not found")
elif ch == 3:
    rollno = int(input("Enter rollno"))
    name = input("Enter name to be updated corresponding to rollno")
    for record in list1:
        if record["rollno"] == rollno:
            record["name"] = name
            break
        else:
            print("Record not found")
else:
    rollno = int(input("Enter rollno"))
    for record in list1:
        if record["rollno"] == rollno:
            list1.remove(record)
    print(list1)

 