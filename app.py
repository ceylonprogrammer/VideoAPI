from flask import Flask
from flask import render_template, stream_with_context
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify
from flask import request, Response

from email.mime.multipart import MIMEMultipart

from datetime import datetime, timedelta
from simpleflake import simpleflake
from pymongo import MongoClient, DESCENDING

import os
import socket
import json
import smtplib
import jinja2
import subprocess
import base64

# Create Database connection with pymongo
print(socket.gethostbyaddr(socket.gethostname()))

# DB Connection

db_client = MongoClient('localhost', 27017)
# print(db_client.server_info()) get connection Details
print("Mongodb Connection Successful")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
