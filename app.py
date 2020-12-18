from main import *
from flask import render_template
from flask import Flask, request
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/",  methods=['GET'])
def home():
    tag = "lofi"
    if(request.args.get('tag')):
        tag = request.args.get('tag')

    streams = getStreams(tag, maxResults=20)
    return render_template("home.html", streams=streams, tag=tag)

if __name__ == "__main__":
    app.run(debug=True)