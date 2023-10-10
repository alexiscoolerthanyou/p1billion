import os
from flask import Flask, request, redirect, url_for, send_file, render_template
from twilio.jwt.access_token.grants import SyncGrant

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()