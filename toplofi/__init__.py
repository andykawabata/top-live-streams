from flask import Flask
from config import Config
from . import home

app = Flask(__name__)
app.config.from_object(Config)


