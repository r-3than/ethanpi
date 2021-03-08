  
from flask import Flask, render_template ,redirect,request
import threading
import time, platform
import datetime
import ctypes, sys
import string , random , bluetooth

app = Flask(__name__)

@app.route("/")
def index():
    bluetooth_devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)

    number_of_devices = len(bluetooth_devices)

    print(number_of_devices,"devices found")
    addresses = []
    names = []
    device_classes = []
    for addr, name, device_class in bluetooth_devices:
        addresses.append(addr)
        names.append(name)
        device_classes.append(device_class)
    return render_template("index.html",devices=names)

app.run(port=5002,debug=False,host="0.0.0.0")