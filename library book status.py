records = []
available_count = 0
issued_count = 0

print("Enter book title (or 'done' to stop):")

while True:
    title = input("Book Title: ")
    if title.lower() == "done":
        break
    author = input("Author: ")
    status = input("Status (Available/Issued): ").capitalize()

    records.append((title, author, status))

    if status == "Available":
        available_count += 1
    elif status == "Issued":
        issued_count += 1

print("\n===== LIBRARY RECORDS =====")
print(f"{'No.':<4}{'Title':<15}{'Author':<10}{'Status':<10}")
print("-" * 38)

for i, (title, author, status) in enumerate(records, start=1):
    print(f"{i:<4}{title:<15}{author:<10}{status:<10}")

print("-" * 38)
print(f"Available: {available_count}  |  Issued: {issued_count}")

with open("library_records.txt", "a") as f:
    f.write("\n===== LIBRARY RECORDS =====\n")
    f.write(f"{'No.':<4}{'Title':<15}{'Author':<10}{'Status':<10}\n")
    f.write("-" * 38 + "\n")
    for i, (title, author, status) in enumerate(records, start=1):
        f.write(f"{i:<4}{title:<15}{author:<10}{status:<10}\n")
    f.write("-" * 38 + "\n")
    f.write(f"Available: {available_count}  |  Issued: {issued_count}\n")

print("Records saved to library_records.txt")
