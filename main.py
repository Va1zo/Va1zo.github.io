import json
import os
from flask import Flask, request, redirect, url_for, render_template, session, send_file, jsonify
from urllib.parse import quote
import random; import sys

##############
app = Flask("Va1zo")

@app.route('/')
def home():
  return render_template("index.html")



app.run(host='0.0.0.0', port=8080)