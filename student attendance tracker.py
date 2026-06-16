students=["Alice","Bob","Carol","Ravi","Raja"]
present=0
absent=0
print("===== ATTENDANCE TRACKER =====")
for name in students:
    status=input("enter a name: ").lower()
    if status in [s.lower() for s in students]: 
        present+=1
        print(present)
    else:
        absent+=1
        print(absent)
total_students = len(students)
attendance_percentage = (present/total_students) * 100
print("\n----------------------------")
print(f"Present : {present}")
print(f"Absent  : {absent}")
print(f"Attendance: {attendance_percentage}%")
