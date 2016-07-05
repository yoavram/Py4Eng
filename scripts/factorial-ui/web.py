#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Yoav Ram <yoav@yoavram.com>
import os
import json
from flask import Flask, jsonify

from cli import factorial

app = Flask(__name__)

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/<int:n>')
def calc(n=10):
	n_factorial = factorial(n)
	return jsonify(result=n_factorial)

if __name__=='__main__':
	app.run(host='127.0.0.1', port=5000, debug=False)
	app.logger.info("Server shutting down")
