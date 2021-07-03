from flask import Flask, render_template

app = Flask(__name__) # instatiating the flask module to this variable so python knows where to look for 


# Routes
@app.route("/") #default page that opens
#the home page- where the todolist will show up
def home():
    #return "this is where the todo list is"
    return render_template('home.html')


@app.route("/login") 
def login():
    #return "this is the login page"
    return render_template('login.html')

@app.route("/register") #aka sign-up page- where a new user makes an account
def register():
    #return "this is the sign up page"
    return render_template('register.html')

@app.route("/report")
def report():
    #return "this is the report page"
    return render_template("report.html")

if __name__=='__main__': # type "python Todolist.py" to get the web server start working
    app.run(debug=True)
