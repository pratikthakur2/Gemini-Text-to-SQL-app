import sqlite3

#connection 
connection= sqlite3.connect("student.db")

#create cursor
cursor=connection.cursor()

#create table

table_info="""
Create table STUDENT(NAME VARCHAR (25), CLASS VARCHAR (25),
SECTION VARCHAR (25), MARKS INT);

"""

cursor.execute(table_info)

#insert records
cursor.execute('''Insert Into STUDENT values( 'Shanu', 'Data Science', 'A',90) ''')
cursor.execute('''Insert Into STUDENT values ('Pratik', 'Data Science', 'B' ,100) ''')
cursor.execute('''Insert Into STUDENT values ('Rahul', 'Data Science', 'A', 86) ''')
cursor.execute('''Insert Into STUDENT values ('Amaan', 'DEVOPS', 'A', 50) ''')
cursor.execute(''' Insert Into STUDENT values ('Krish', 'DEVOPS', 'A', 35)''')

#display records
print("The insterted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

#close the connection
    
connection.commit()
connection.close()