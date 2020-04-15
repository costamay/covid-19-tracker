from flask import Flask, jsonify, request, Response, g
from src.estimator import estimator
from dicttoxml import dicttoxml 
import os
import time
import json
import logging

if "requests.txt" in os.listdir():
    os.remove("requests.txt")
    
app = Flask(__name__)

logging.basicConfig(filename='requests.txt', level=logging.INFO)

@app.before_request
def get_time():
    g.start_time = time.time()

@app.route('/api/v1/on-covid-19/', methods=['POST', 'GET'])
@app.route('/api/v1/on-covid-19/json', methods=['POST', 'GET'])
def covid_json():
    if request.method == "GET":
        res = Response("", content_type="application/json")
        return res, 200

    if request.method == "POST":
        data = request.get_json()
        output = estimator(data)
        return jsonify(output), 200
    
    # data = request.get_json()
    # output = estimator(data)
    # return jsonify(output), 200
    
@app.route('/api/v1/on-covid-19/xml', methods=['POST', 'GET'])
def covid_xml():
    if request.method == "GET":
        res = Response("", content_type="application/xml")
        return res, 200

    if request.method == "POST":
        data = request.get_json()
        output = estimator(data)
        res = \
            Response(dicttoxml(
                output, attr_type=False),
                content_type="application/xml")
        return res, 200
    
    # data = request.get_json()
    # output = estimator(data)
    # res = \
    #     Response(dicttoxml(
    #         output, attr_type=False),
    #         content_type="application/xml")
    # return res, 200
    
    
    

@app.route('/api/v1/on-covid-19/logs', methods=['GET', 'POST'])
def logs():
    logs = []  
    with open("requests.txt", "rt") as f:   # read logs file 
        data = f.readlines()
    for line in data:
        if "root" in line and "404" not in line:
            logs.append(line[10:])

    return Response("".join(logs), mimetype="text/plain")

@app.after_request
def log_request_info(response):
    response_time = int((time.time() - g.start_time) * 1000)
    status_code = response.status.split()[0]
    logging.info(
        f"{request.method}\t\t{request.path}\t\t{status_code}\t\t{str(response_time).zfill(2)}ms\n"
    )

    return response


if __name__ == '__main__':
    app.run(debug = True)