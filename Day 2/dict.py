student ={
    "name":"manish",
    "class":"math",
    "Time":"10:00 am"
}

print(student["Time"])


student["Teacher"]= "Rama"

print(student)


del student["name"]
print(student)


employees = {}

def add_employee(key, value):
    employees[key] = value
    print(f"stored {key} = {value}")


print("Add Employee Data")
key1 = input(str("Enter Key Value "))
value1 = input(str("Enter Value "))

add_employee(key1, value1)



def display_employee():
    for key,value in employees:
        print(f"{key}={value}")







# temp_memory = {}

# def store_data(key, value):
#     temp_memory[key] = value
#     print(f"Stored: {key} → {value}")

# def get_data(key):
#     if key in temp_memory:
#         print(f"Retrieved: {key} → {temp_memory[key]}")
#     else:
#         print(f"Key '{key}' not found in memory.")

# def show_memory():
#     print("Current Memory:")
#     for key, value in temp_memory.items():
#         print(f"  {key} → {value}")

# store_data("name", "Manish")
# store_data("age", 25)
# get_data("name")
# get_data("city")
# show_memory()