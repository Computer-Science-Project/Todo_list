import mysql.connector

mysqlcon=mysql.connector.connect(host="localhost", user="root", passwd=input("Enter your MySQL password: "), database="todo_list")
cursor=mysqlcon.cursor()

def valid_login(username, password):
    cursor.execute("select password from users where username='"+username+"';")
    correct_password=cursor.fetchone()[0]
    mysqlcon.close()
    print(correct_password)
    if password==correct_password:
        return True
    else:
        return False


