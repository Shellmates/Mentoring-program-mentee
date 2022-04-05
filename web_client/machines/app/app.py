import http
from flask import Flask, render_template, send_from_directory, request, make_response

app = Flask(__name__, static_folder='static')


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, "robots.txt")

@app.route('/s333333333cr3t')
def secret():
    return "<h3>can't even hide my secrets any more :/</h3> <h3>shellmates{beep_b00p_beep_b3ep_?}<h3>"

if __name__=="__main__":
    app.run()