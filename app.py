from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

purchase_server_working = True
website_title = "EGrocery"

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('server-status')
def get_server_status():
    pur_ser_str = "ERROR RETRIEVING STATUS"

    if purchase_server_working == True:
        pur_ser_str = "OK"
    else:
        pur_ser_str = "DOWN"

    return f"""
    <h1>Server Status</h1>
    <h4>Website Server: OK</h4>
    <h4>Purchase Server: {pur_ser_str}</h4>"""

@app.route('/')
def home():
    return render_template('index.html', title=website_title, pur_ser=purchase_server_working)
