import subprocess
from flask import Flask, flash, request, redirect, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" : 
        folder = request.form.get("folder")
        if folder :
            if " " in folder :
                    return render_template("index.html",statement="That's not allowed") 
            else : 
                try : 
                    out = subprocess.run(f"ls {folder}", shell=True, timeout=2, capture_output=True).stdout.decode()
                    return render_template("index.html",statement=out)
                except  :
                    return render_template("index.html",statement="Something went wrong and I'm too lazy to investigate")
        else :
            return render_template("index.html",statement="Folder can't be empty string")
    return render_template("index.html",statement="") 
# Error handling

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
