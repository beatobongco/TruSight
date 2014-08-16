from flask import Flask, render_template

app = Flask(__name__)

# Base config
app.config.from_object('config')

from . import views