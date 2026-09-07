"""Calculate an electricity bill from units consumed."""

# Read the customer's electricity usage.
customer_name = input("Enter customer name: ")
units_consumed = float(input("Enter electricity units consumed: "))

# Apply a simple slab-based tariff.
if units_consumed <= 100:
    bill_amount = units_consumed * 1.50
elif units_consumed <= 200:
    bill_amount = (100 * 1.50) + ((units_consumed - 100) * 2.50)
elif units_consumed <= 500:
    bill_amount = (100 * 1.50) + (100 * 2.50) + ((units_consumed - 200) * 4.00)
else:
    bill_amount = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units_consumed - 500) * 6.00)

fixed_charge = 50.00
total_bill = bill_amount + fixed_charge

print("\nElectricity Bill")
print(f"Customer: {customer_name}")
print(f"Units consumed: {units_consumed:.2f}")
print(f"Energy charge: {bill_amount:.2f}")
print(f"Fixed charge: {fixed_charge:.2f}")
print(f"Total bill: {total_bill:.2f}")
