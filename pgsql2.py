import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="student_record",   # change this
    user="postgres",
    password="nithish@07",
    port="5432"
)

cursor = conn.cursor()

# Insert query
query = """
INSERT INTO users (name, email)
VALUES (%s, %s)
"""
data=[]
name = input("enter name: ")
data.append(name)
mail=input("enter your email: ")
data.append(mail)

cursor.execute(query, data)
conn.commit()

print("Data inserted successfully")

# Fetch data to verify
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()