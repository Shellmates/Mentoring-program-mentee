import os
from flask import Flask, request, redirect, render_template, render_template_string, send_file
from dotenv import load_dotenv
import re

load_dotenv()

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config["DEBUG"] = os.getenv("FLASK_ENV") == "development"

# Routes

@app.route("/", methods=["GET"])
def index():
    page = request.args.get("page")
    path = f"{APP_ROOT}/templates/{page}"
    if not page:
        return redirect("/?page=index.html")
    elif page == "index.html":
        return render_template("index.html")
    elif os.path.exists(path):
        return send_file(path)
    else:
        return f"Page '{path}' does not exist"

# Error handlers

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
