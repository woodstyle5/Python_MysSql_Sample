__author__ = 'Mary Grace'
import MySQLdb


#Setting up Connection
db = MySQLdb.connect("127.0.0.1","root","passes12345","try_student")
cursor = db.cursor()

studId=raw_input("Enter Student Id: ")
name = raw_input("Enter Student Naame: ")
grade=raw_input("Enter Student Grade: ")


sql = "Insert into student(studentID, studentName)\
      Values ('%s', '%s')" % \
      (studId, name)

try:
    cursor.execute(sql)
    db.commit()
    print "Data was Added"
except:
    db.rollback()
    print "There is a problem encountered"



db.close()

