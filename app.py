# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='Hackathon Website')

import assigments

purchase_server_working = True
website_title = "EGrocery"


@app.route("/")
def serve():
    return send_from_directory('', 'index.html')


@app.route('/server-status')
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


'''
@app.route('/')
def home():
    return render_template('index.html',
                           title=website_title,
                           pur_ser=purchase_server_working)
'''

assigments.init(app)
