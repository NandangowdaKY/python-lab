import csv
import matplotlib.pyplot as plt

dates = {}
products = {}

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row["Date"]
        product = row["Product"]
        sales = int(row["Sales"])

        dates[date] = dates.get(date, 0) + sales
        products[product] = products.get(product, 0) + sales

print("RETAIL SALES REPORT")

for date in sorted(dates):
    print(f"{date}: {dates[date]}")

print("\nProduct Wise Sales")

for product, sales in products.items():
    print(f"{product}: {sales}")

plt.figure(figsize=(8, 5))
plt.plot(
    sorted(dates),
    [dates[date] for date in sorted(dates)],
    marker="o"
)

plt.title("Daily Retail Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(products.keys(), products.values())

plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
