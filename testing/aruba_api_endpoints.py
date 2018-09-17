from flask import Flask, request, jsonify
from flask_restful import Resource
import json, urllib.parse

class login(Resource):
  def __init__(self):
    pass

  def get(self):
    loginOK = True
    login_data = urllib.parse.parse_qs(urllib.parse.urlparse(request.url).query)
   
    if login_data["username"][0] != "testuser":
      loginOK = False
    if login_data["password"][0] != "password123":
      loginOK = False

    if loginOK:
      response = json.loads('{"_global_result": {"status":"0", "status_str": "You\'ve logged in successfully.", "UIDARUBA":"fADCeF6a-cbCC-3DFB-ECED-bEa213EBc3A5"}}')
    else:
      response = json.loads('{"_global_result": {"status":"1", "status_str": "Unauthorized request, authentication failed"}}')

    return response

class logout(Resource):
  def __init__(self):
    pass

  def get(self):
    response = json.loads('{"_global_result": {"status":"0", "status_str": "You\'ve been logged out successfully.", "UIDARUBA":"(null)"}}')
    return response

class write_memory(Resource):
  def __init__(self):
    pass

  def post(self):
    url_data = urllib.parse.parse_qs(urllib.parse.urlparse(request.url).query)
    if url_data["UIDARUBA"][0] == "fADCeF6a-cbCC-3DFB-ECED-bEa213EBc3A5":
      response = json.loads('{"write_memory":{"_result":{"status": 0,"status_str": "Success"}},"_global_result": {"status": 0,"status_str": "Success","_pending": false}}')
    else:
      response = json.loads('{"_global_result":{"status": 1,"status_str": "Invalid authentication token(UIDARUBA) in request URL"}}')

    return response