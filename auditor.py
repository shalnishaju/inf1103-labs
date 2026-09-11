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