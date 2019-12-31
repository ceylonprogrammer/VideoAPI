'''
GET Request for Advanced REST Client
http://127.0.0.1:5000/videoapi/register?json={"fname":"sam","lname":"Dissa","email":"sameerad177@gmail.com","password":"abc123"}
POST Request for Advanced REST Client
application/x-www-form-urlencoded RAW input payload json={"fname":"sam","lname":"Dissa","email":"sameerad177@gmail.com","password":"abc123"}
'''
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
# print(socket.gethostbyaddr(socket.gethostname()))

# DB Connection

db_client = MongoClient('localhost', 27017)
# print(db_client.server_info()) get connection Details

# print("Mongodb Connection Successful")

db = db_client['videoAPI']
user_info = db['userdata']
user_login_info = db['login_info']
video_data = db['video_db']

app = Flask(__name__)
app.debug = True
# Enable debug for Dev Environment

# assign user verification unique id using simpleflake
user_verification_id = simpleflake()
reg_time = datetime.now()

# Enable to share data between java script and python flask .so we use flask CORS

CORS(app)


@app.route('/videoapi/register', methods=['GET', 'POST'])
def user_register():
    # check if it is a GET method
    if request.method == 'GET':
        request_data = request.args
    elif request.method == 'POST':
        request_data = request.form
    else:
        print("Unknown Request Method,Request should be GET or POST method")
    try:
        output = {"success": True, 'date': str(datetime.now())}
        # get URL parameter and then convert it to json object

        # single line initialization
        # json_obj = json.loads(request.args.get('json', ''))

        # Get url argument GET method.Later discuss how to add GET and POST methods
        # request_data = request.args
        # Newly added GET and POST method so this line is commented

        # Get jason type from request.args
        json_obj = request_data.get('json')

        # cast in to json key value pairs
        url_args = json.loads(json_obj)

        # create Empty Dictionary to hold url arguments
        user_details = {}
        user_details['First_Name'] = url_args['fname']
        user_details['Last_Name'] = url_args['lname']
        user_details['email'] = url_args['email']
        user_details['Password'] = url_args['password']
        user_details['User_id'] = user_verification_id
        user_details['Verified'] = False
        user_details['Register_time'] = str(reg_time)

        # Check Existing Email Address

        if user_info.count({"email": user_details['email']}) == 1:
            output['success'] = False
            output['Error'] = "Email Address already Exists,Please use different email address"

        else:

            add_email = user_info.insert(user_details)

    except Exception as ex:
        output['success'] = False
        output['Error'] = str(ex.message)

    return json.dumps(output)


if __name__ == '__main__':
    app.run()
