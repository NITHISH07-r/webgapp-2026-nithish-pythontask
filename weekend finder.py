days=["monday","tuesday","wednesday","thursday","friday"]
weekend=["saturday","sunday"]
day=input("enter a day in a week: ")
if day.lower() in days:
    print("not a weekend")
elif day.lower() in weekend:
    print("weekend")
else:
    print("enter a valid day")