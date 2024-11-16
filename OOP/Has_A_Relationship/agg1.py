class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def __repr__(self):
        return f"Employee(Name: {self.name}, ID: {self.emp_id})"

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.employees = []  # Aggregation: Bank has Employees, but they can exist independently

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        for emp in self.employees:
            print(emp)

# Employees exist independently of the bank
employee1 = Employee("Alice", 101)
employee2 = Employee("Bob", 102)

# Bank aggregates employees
bank = Bank("ABC Bank")
bank.add_employee(employee1)
bank.add_employee(employee2)

# Display employees
print(f"Employees at {bank.bank_name}:")
bank.show_employees()

# Even if the bank is deleted, employees exist
del bank
print(f"Employees still exist: {employee1}, {employee2}")
