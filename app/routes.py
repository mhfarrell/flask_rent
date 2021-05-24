from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from app import app

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
