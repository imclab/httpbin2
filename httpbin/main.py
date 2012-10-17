# -*- coding: utf-8 -*-

from flask import Flask
from werkzeug.wsgi import responder
from werkzeug.utils import redirect

LEGACY_HTTPBIN = 'httpbin.org'

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Examples....'

@responder
def fallback(*args):
    return redirect('http://httpbin.org')