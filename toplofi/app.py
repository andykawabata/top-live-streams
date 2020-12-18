from toplofi.main import *
from flask import render_template
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    streams = getStreams(maxResults=20)
    return render_template("home.html", streams=streams)

if __name__ == "__main__":
    app.run(Debug=True)