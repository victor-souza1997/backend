from flask import Flask, render_template
from flask_pymongo import PyMongo
import os
import json
from flask import Response
from flask import jsonify
from bson.json_util import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ['MONGO_URI']

mongo = PyMongo(app)


@app.route('/input_data/<device_id>/<value>')
def save_data_device(device_id, value):
    try:
        devices = [device for device in mongo.db.devices.find(
            {'device_id': device_id})]
        if devices:
            mongo.db.data.insert_one(
                {'device_id': device_id, 'value': value})
        else:
            return "device not in the system"
    except Exception as e:
        return 'not saved'
    return "saved with sucess"


@app.route('/get_devices')
def get_devices():
    # try:
    devices_list = mongo.db.devices.find()
    devices_list = [device for device in devices_list]
    print(devices_list)
    # print(json.dumps(devices_list))
    if devices_list:
        return Response(json.dumps(devices_list, default=str), mimetype="application/json")

    else:
        return None


@app.route('/set_newdevice/<device_id>')
def set_device(device_id):
    try:
        devices = [device for device in mongo.db.devices.find(
            {'device_id': device_id})]
        if devices:
            return "already up"
        mongo.db.devices.insert_one(
            {'device_id': device_id})
    except:
        return 'not saved'
    return "saved with sucess"


@ app.route('/get_data/<device_id>')
def get_data(device_id):
    data_list = mongo.db.data.find({'device_id': device_id})
    datas = [data for data in data_list]
    return Response(json.dumps(datas, default=str), mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)
