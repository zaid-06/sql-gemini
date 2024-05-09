import sqlite3

## connet to sqlite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record , create table 
cursor = connection.cursor()

# create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(NAME  VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""
cursor.execute(table_info)

# insert some more records 
cursor.execute("""Insert Into STUDENT values('zaid','Data science', 'A')""")
cursor.execute("""Insert Into STUDENT values('krish','DEVOPS', 'B')""")
cursor.execute("""Insert Into STUDENT values('don','DEVOPS', 'A')""")
cursor.execute("""Insert Into STUDENT values('Shabab','engineer', 'A')""")
cursor.execute("""Insert Into STUDENT values('Rahman','cunstructor', 'A')""")

print("The inserted records are ")
data = cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)

connection.commit()
connection.close()



