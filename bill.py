# electricity_bill.py

def calculate_bill(units):
    rate_per_unit = 5
    total_bill = units * rate_per_unit
    discount = 0

    if total_bill > 1000:
        discount = total_bill * 0.10

    final_bill = total_bill - discount

    print(f"Units Consumed: {units}")
    print(f"Total Bill: ₹{total_bill}")
    print(f"Discount Applied: ₹{discount}")
    print(f"Final Bill: ₹{final_bill}")

# Example usage
calculate_bill(250)
