import mysql.connector
mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="raman")
mysqlcursor = mysqldb.cursor()
#create Table
'''
mysqlcursor.execute(
"create table student(rollno INT , name VARCHAR(30) , marks INT)")


#insert into table

try:
    
    mysqlcursor.execute("insert into student(rollno , name , marks) values(2 , 'Raju' , 98) ")
    mysqldb.commit()
    print("Record inserted into the table")
except:
    mysqldb.rollback()
mysqldb.close()

#display Record 

try:
    mysqlcursor.execute("select * from student where rollno = 1941043")
    result = mysqlcursor.fetchall()
    for i in result:
        roll = i[0]
        name = i[1]
        marks = i[2]
        print(roll , name , marks)
        
except:
    print("Some issue in the code")
mysqlcursor.close()

#to update the record


try:
    mysqlcursor.execute("update student set name='Sachin' where rollno = 1941043")
    mysqldb.commit()
    print("Record updated successfully")
except:
    print("Record not found")
    mysqldb.rollback()
mysqlcursor.close()



# To Perform Delete Operation

try:
    mysqlcursor.execute("delete from  student  where rollno = 2")
    mysqldb.commit()
    print("Record deleted successfully")
except:
    print("Record not found")
    mysqldb.rollback()
mysqlcursor.close()
'''