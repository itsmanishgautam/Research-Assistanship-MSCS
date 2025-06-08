import csv
import os

# Separate config for file path
FILE_DIR = 'day 1/employee management console'
FILE_NAME = 'employees.csv'
filename = os.path.join(FILE_DIR, FILE_NAME)

def load_employees():
    if not os.path.isfile(filename):
        return []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_employee(emp):
    os.makedirs(FILE_DIR, exist_ok=True)  # ensure directory exists
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Age', 'Salary', 'Department'])
        writer.writerow([emp['Name'], emp['Age'], emp['Salary'], emp['Department']])
    print("Employee data saved.")

def employee_add():
    ename = input("Enter employee name: ")
    eage = input("Enter employee age: ")
    esalary = input("Enter monthly salary: ")
    edepartment = input("Enter department: ")
    emp = {'Name': ename, 'Age': eage, 'Salary': esalary, 'Department': edepartment}
    save_employee(emp)

def view_all():
    employees = load_employees()
    if not employees:
        print("No employee data found.")
        return
    print("All Employees:")
    for e in employees:
        print(f"{e['Name']}, Age: {e['Age']}, Salary: {e['Salary']}, Department: {e['Department']}")

def average_salary():
    employees = load_employees()
    if not employees:
        print("No employee data to calculate average salary.")
        return
    total = 0
    count = 0
    for e in employees:
        try:
            total += float(e['Salary'])
            count += 1
        except ValueError:
            continue
    if count == 0:
        print("No valid salary data found.")
        return
    print(f"Average Salary: {total / count:.2f}")

def employees_by_department():
    employees = load_employees()
    if not employees:
        print("No employee data found.")
        return
    dept = input("Enter department name to filter: ")
    filtered = [e for e in employees if e['Department'].lower() == dept.lower()]
    if not filtered:
        print(f"No employees found in department '{dept}'.")
        return
    print(f"Employees in department {dept}:")
    for e in filtered:
        print(f"{e['Name']}, Age: {e['Age']}, Salary: {e['Salary']}")

def highest_paid_employee():
    employees = load_employees()
    if not employees:
        print("No employee data found.")
        return
    highest = None
    for e in employees:
        try:
            salary = float(e['Salary'])
        except ValueError:
            continue
        if highest is None or salary > highest['Salary']:
            highest = {'Name': e['Name'], 'Age': e['Age'], 'Salary': salary, 'Department': e['Department']}
    if highest:
        print(f"Highest Paid Employee: {highest['Name']}, Salary: {highest['Salary']}, Department: {highest['Department']}")
    else:
        print("No valid salary data found.")

def main():
    while True:
        print("\nWelcome to Employee Management Console")
        print("1) Enter Employee Details")
        print("2) View All Employee Details")
        print("3) Show Average Salary")
        print("4) Show Employees by Department")
        print("5) Show Highest Paid Employee")
        print("6) Exit")

        choice = input("Enter number: ")

        if choice == '1':
            employee_add()
        elif choice == '2':
            view_all()
        elif choice == '3':
            average_salary()
        elif choice == '4':
            employees_by_department()
        elif choice == '5':
            highest_paid_employee()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
