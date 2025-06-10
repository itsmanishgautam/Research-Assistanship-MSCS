temp_memory = {}

def store_data(key, value):
    temp_memory[key] = value
    print(f"Stored: {key} → {value}")

def get_data(key):
    if key in temp_memory:
        print(f"Retrieved: {key} → {temp_memory[key]}")
    else:
        print(f"Key '{key}' not found in memory.")

def show_memory():
    print("Current Memory:")
    for key, value in temp_memory.items():
        print(f"  {key} → {value}")

store_data("name", "Manish")
store_data("age", 25)
get_data("name")
get_data("city")
show_memory()

student ={
    "name":"manish",
    "class":"math",
    "Time":"10:00 am"
}

print(student["Time"])


student["Teacher"]= "Rama"

print(student)