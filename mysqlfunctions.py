import mysql.connector

def valid_login(username, password):
    mysqlcon=mysql.connector.connect(host="localhost", user="root", passwd=input("Enter your MySQL password: "), database="todo_list")
    cursor=mysqlcon.cursor()
    cursor.execute("select password from users where username='"+username+"';")
    correct_password=cursor.fetchone()[0]
    mysqlcon.close()
    return password==correct_password

def registration(username, password):
    mysqlcon=mysql.connector.connect(host="localhost", user="root", passwd=input("Enter your MySQL password: "), database="todo_list")
    cursor=mysqlcon.cursor()
    cursor.execute("insert into users values ('"+username+"','"+password+"');")
    cursor.commit()
    mysqlcon.close()

def change_username(old, new):
    mysqlcon=mysql.connector.connect(host="localhost", user="root", passwd=input("Enter your MySQL password: "), database="todo_list")
    cursor=mysqlcon.cursor()
    cursor.execute("update users set username='"+new+"' where username='"+old+"';")
    cursor.commit()
    mysqlcon.close()

def delete_user(username):
    mysqlcon=mysql.connector.connect(host="localhost", user="root", passwd=input("Enter your MySQL password: "), database="todo_list")
    cursor=mysqlcon.cursor()
    cursor.execute("delete from users where username='"+username+"';")
    cursor.commit()
    mysqlcon.close()


