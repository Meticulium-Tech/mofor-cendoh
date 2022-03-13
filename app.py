from flask import Flask, jsonify, render_template
import gspread
import json

app = Flask(__name__)


@app.route("/")
def home():
    render_template("index.html", lorem='ipsum')
