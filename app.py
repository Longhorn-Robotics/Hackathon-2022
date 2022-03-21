# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='Hackathon Website')

import assigments


@app.route("/")
def serve():
    return send_from_directory('', 'index.html')


assigments.init(app)
