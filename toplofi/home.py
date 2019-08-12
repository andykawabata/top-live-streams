from toplofi import app
from toplofi.main import *
from flask import render_template

@app.route("/")
def home():
    streams = getStreams(maxResults=15)
    return render_template("home.html", streams=streams)
