#!/usr/bin/python3
from flask import Flask, Response, request, render_template, make_response

app = Flask(__name__)


@app.route("/",methods = ["GET"])
def main():
    cookie = request.cookies.get("admin")
    if not cookie : 
        resp = make_response(render_template('admin.html', admin=False))
        resp.set_cookie("admin","0")
        return resp 

    elif cookie == "1" :
        return render_template('admin.html', admin=True)

    else :
        return render_template('admin.html', admin=False)
