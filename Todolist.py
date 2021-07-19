from flask import Flask, render_template, request
import mysqlfunctions

app = Flask(__name__) # instantiating the flask module to this variable so python knows where to look for

from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # instatiating the flask module to this variable so python knows where to look for 
app.config['SECRET_KEY'] = 'c5b001929f7e9cba838cd7a922db0dec'

# Routes
@app.route("/") #default page that opens
#the home page- where the todolist will show up
def home():
    #return "this is where the todo list is"
    return render_template('home.html')

@app.route("/login") 
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

@app.route("/register") #aka sign-up page- where a new user makes an account
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)

@app.route("/report")
def report():
    return "this is the report page"
    #return render_template("report.html")

if __name__=='__main__': # type "python Todolist.py" to get the web server start working
    app.run(debug=True)
