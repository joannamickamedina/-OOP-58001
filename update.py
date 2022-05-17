import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\ginae\Downloads\Database2.accdb;')
    print("Connected to a Database")

    Fullname = 'Medina, Joanna Micka E.'
    Assignment = 95
    Laboratory = 100
    Quiz = 98
    Exam = 100
    user_id = 10

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ? WHERE id= ?',(Fullname, user_id))
    record.execute('UPDATE Table1 SET Assignment = ? WHERE id= ?', (Assignment, user_id))
    record.execute('UPDATE Table1 SET Laboratory = ? WHERE id= ?', (Laboratory, user_id))
    record.execute('UPDATE Table1 SET Quiz = ? WHERE id= ?', (Quiz, user_id))
    record.execute('UPDATE Table1 SET Exam = ? WHERE id= ?', (Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")
