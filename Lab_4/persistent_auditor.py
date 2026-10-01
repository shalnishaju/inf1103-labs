import json


def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit' to finish): ")

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        return None

    return int(user_input)


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("\n--- Inventory Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            data = json.load(file)
            return data["inventory"], data["history"]
    except FileNotFoundError:
        return 0, []


def save_inventory(inventory, transaction_history):
    data = {
        "inventory": inventory,
        "history": transaction_history
    }

    with open("inventory.txt", "w") as file:
        json.dump(data, file, indent=4)


def main():
    inventory, transaction_history = load_inventory()
    failed_entries = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            save_inventory(inventory, transaction_history)
            break

        if result is None:
            failed_entries += 1
            continue

        quantity = result
        transaction_history.append(quantity)

        inventory = process_delivery(inventory, quantity)

        tax = calculate_tax(quantity)
        print("Tax for this delivery:", tax)

        if inventory > 500:
            print("OVERSTOCK ALERT!")
            save_inventory(inventory, transaction_history)
            break

    print("Transaction History:", transaction_history)
    generate_report(inventory, failed_entries)


if __name__ == "__main__":
    main()