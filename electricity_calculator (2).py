# Electricity Bill Calculator
RATE = 12.90

# Validate name
while True:
    name = input("Enter customer name: ")

    if name.strip() != "":
        break
    else:
        print("Invalid name. Please try again.")

# Validate previous reading
while True:
    previous = float(input("Enter previous meter reading: "))
    
    if previous >= 0:
        break
    else:
        print("Invalid previous meter reading. Number must be at least 0. Please try again.")

# Validate current reading
while True:
    current = float(input("Enter current meter reading: "))
    
    if current >= previous:
        break
    else:
        print("Invalid reading. Number must be at least the previous reading. Please try again.")

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
