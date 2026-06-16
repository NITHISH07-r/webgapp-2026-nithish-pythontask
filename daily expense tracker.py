from datetime import datetime

today = datetime.today().date()
print(f"Date: {today}")

expenses = []
print("\nEnter expense (or 'done' to stop):")
while True:
    item = input("Item: ")
    if item.lower() == "done":
        break
    amount = float(input("Amount: "))
    expenses.append((item, amount))

total = sum(amount for _, amount in expenses)

print("\n===== EXPENSE SUMMARY =====")
print(f"Date: {today}")
for item, amount in expenses:
    print(f"{item:<10} : Rs. {amount:<10}")
print("-" * 27)
print(f"Total     : Rs. {total: }")
with open("expenses.txt", "a") as f:
    f.write("\n===== EXPENSE SUMMARY =====\n")
    f.write(f"Date: {today}\n")
    for item, amount in expenses:
        f.write(f"{item:<10} : Rs. {amount:<10}\n")
    f.write("-" * 27 + "\n")
    f.write(f"Total     : Rs. {total:<10}\n")

print("Saved to expenses.txt")
