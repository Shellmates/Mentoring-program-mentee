#!/usr/bin/python3

from flask import Flask, request, render_template, redirect, url_for, make_response
from bot import admin_check
import json
import base64 as b64
from urllib import parse

app = Flask(__name__)

users = {"admin":"jsu4398jdoy98lkdfjlkjxo8"}
notes = []
vuln = "<span>{message}<br/></span><br/><hr/>"

@app.route("/", methods=["GET", "POST"])
def root():
    return redirect("home") 


@app.route("/home",methods=["GET","POST"])
def home():
    title, mssg = request.args.get("title"), request.args.get("message")
    if title and mssg : 
        with open("bad.html") as f :
            return f.read().format(title=title,message=mssg)
    return render_template('index.html')  

    return redirect('/login')

@app.route("/send",methods=["GET","POST"])
def send():
    if request.method == "GET" : 
        return render_template("send.html")
    url = request.form.get("url")
    if url : 
        args = parse.parse_qs(parse.urlparse(url).query)
        if "title" in args and "message" in args : 
            title, mssg = args["title"][0], args["message"][0]   
            try : 
                admin_check(title,mssg)             
            except : 
                return render_template("view.html",result="something bad happened")
            return render_template("view.html",result="Admin will soon view your note")
    return render_template("view.html",result="Invalid url")

