class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if emp.name.lower() == target_name.lower()]
        return result

    def search_by_salary(self, operator, target_salary):
        if operator == '>':
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == '<':
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == '>=':
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        elif operator == '<=':
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            result = []
        return result

if __name__ == "__main__":
    table = EmployeeTable()

    table.add_employee(Employee("161E90", "Raman", 41, 56000))
    table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    search_param = input("Enter search parameter (1. Age, 2. Name, 3. Salary): ")

    if search_param == '1':
        target_age = int(input("Enter age to search: "))
        result = table.search_by_age(target_age)
    elif search_param == '2':
        target_name = input("Enter name to search: ")
        result = table.search_by_name(target_name)
    elif search_param == '3':
        operator = input("Enter salary operator (> < >= <=): ")
        target_salary = float(input("Enter salary to compare: "))
        result = table.search_by_salary(operator, target_salary)
    else:
        result = []

    if result:
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found.")
