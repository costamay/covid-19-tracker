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

@app.route('/api/v1/on-covid-19/', methods=['POST'])
@app.route('/api/v1/on-covid-19/json', methods=['POST'])
def covid_json():
    request_data = request.get_json()
    data = estimator(request_data)
    
    response = Response(json.dumps(data), 200, mimetype='application/json')
    response.headers['Location'] = ("/api/v1/on-covid-19/json")
    return response
    # return jsonify(data)
    
@app.route('/api/v1/on-covid-19/xml', methods=['POST'])
def covid_xml():
    request_data = request.get_json()
    data = estimator(request_data)
    
    res = Response(dicttoxml(data, attr_type=False), status=200,  content_type="application/xml")
    res.headers['Location'] = ("/api/v1/on-covid-19/xml")
    return res
    # return dicttoxml(data)

@app.route('/api/v1/on-covid-19/logs', methods=['GET'])
def logs():
    logs = []  
    with open("requests.txt", "rt") as f:   # read logs file 
        data = f.readlines()
    for line in data:
        if "root" in line and "404" not in line:
            logs.append(line[20:])

    return Response("".join(logs), mimetype="text/plain")

@app.after_request
def log_request_info(response):
    response_time = int((time.time() - g.start) * 1000)
    status_code = response.status.split()[0]
    logging.info(
        f"{request.method}\t\t{request.path}\t\t{status_code}\t\t{str(response_time).zfill(2)}ms\n"
    )

    return response


if __name__ == '__main__':
    app.run(debug = True)