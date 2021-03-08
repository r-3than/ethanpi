  
from flask import Flask, render_template ,redirect,request
import threading
import time, platform
import datetime
import ctypes, sys
import string , random

app = Flask(__name__)

@app.route("/")
def index():
    f = ["test"]
    return render_template("index.html",webpages=f)

app.run(port=5002,debug=False,host="0.0.0.0")