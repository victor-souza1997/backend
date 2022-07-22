from flask import Flask, render_template
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ['MONGO_URI']

mongo = PyMongo(app)


@app.route('/input_data/<sensor_id>/<value>')
def save_data_sensor(sensor_id, value):
    try:
        mongo.db.data.insert_one(
            {'sensor': sensor_id, 'value': value})
    except Exception as e:
        return 'not saved'
    return "saved with sucess"


@app.route('/get_devices')
def get_devices():
    try:
        devices_list = mongo.db.devices.find()
    except:
        return 'not found'
    return str(devices_list)


@app.route('/set_newdevice/<sensor_id>')
def set_device():
    try:
        mongo.db.devices.insert_one(
            {'device': 'device_id',
             'name': 'device_name',
             'type': 'device_type',
             'status': 'device_status'})

    except:
        return 'not saved'
    return "saved with sucess"


@ app.route('/get_data/<sensor_id>')
def get_data(sensor_id):
    data_list = mongo.db.data.find({'sensor': sensor_id})
    datas = [data for data in data_list]
    return str(datas)


if __name__ == '__main__':
    app.run(debug=True)
