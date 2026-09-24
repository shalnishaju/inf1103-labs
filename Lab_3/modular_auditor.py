inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or quit): ")

    if user_input == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        failed_entries += 1
        continue

    quantity = int(user_input)

    inventory += quantity

    if inventory > 500:
        print("OVERSTOCK ALERT!")
        break

print("\nTotal Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)

# new modular_auditor
# get_valid_input()
#     Input: nothing
#     Output: valid integer OR quit signal

# process_delivery(current_total, new_value)
#     Input: current total + delivery amount
#     Output: new total

# calculate_tax(amount)
#     Input: delivery amount
#     Output: 10% tax

# generate_report(total_units, failed_attempts)
#     Input: final total + failed attempts
#     Output: prints report
def get_valid_input():
    while True:
        user_input = input("Enter stock quantity (or 'quit' to finish): ")
        if user_input.lower() == "quit":
            return "quit"
        try:
            value = int(user_input)
            if value < 0:
                print("Error: Stock quantity cannot be negative.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):