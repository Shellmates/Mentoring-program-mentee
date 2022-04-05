from flask import Flask, request, redirect, render_template, render_template_string
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)



# Routes

@app.route("/", methods=["GET","POST"])
def index():
    statement = ""
    if request.method == "POST" : 
        name = request.form.get("name")
        if name :
            try : 
                statement = "Welcome Mentee : "+render_template_string(name)
            except : pass
    return render_template("index.html",statement=statement) 


# Error handlers

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
