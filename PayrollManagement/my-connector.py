import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    port='3306',
    database='payroll_mngmt'
)


mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM tbl_user')
emp_records = mycursor.fetchall()
for user in emp_records:
    print(user)
    print('Username - '+user[1])