def take_attendance():
    students = ["Alice", "Bob", "Carol", "David", "Eve"]
    attendance = {}

    print("===== ATTENDANCE TRACKER =====")
    for name in students:
        status = input(f"Mark attendance for {name} (P/A): ").upper()
        while status not in ("P", "A"):
            status = input("  Enter P or A: ").upper()
        attendance[name] = status

    present = sum(1 for s in attendance.values() if s == "P")
    absent = len(students) - present
    percentage = (present / len(students)) * 100

    print("\n===== SUMMARY =====")
    for name, status in attendance.items():
        print(f"{name:<10} : {status}")
    print(f"\nPresent    : {present}")
    print(f"Absent     : {absent}")
    print(f"Attendance : {percentage:.1f}%")

take_attendance()
