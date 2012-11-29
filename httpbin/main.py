# -*- coding: utf-8 -*-

import os

import requests
from flask import Flask, request, Response
# from werkzeug.wsgi import responder
# from werkzeug.utils import redirect

LEGACY_HTTPBIN = os.environ.get('LEGACY_HTTPBIN', 'httpbin.org')


def convert_response(r):
    """Creates a Flask Response object from a Requests Response object."""

    return Response(r.content, status=r.status_code, headers=r.headers)


app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
    return 'Examples....'

@app.errorhandler(404)
def legacy_proxy(e):

    url = 'http://{domain}/{path}'.format(
        domain=LEGACY_HTTPBIN,
        path=request.environ['RAW_URI']
    )

    headers = dict(request.headers.to_list())
    del headers['Host']

    r = requests.get(url, headers=headers)
    return convert_response(r)