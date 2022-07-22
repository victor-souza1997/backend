from flask import Flask, render_template
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ['MONGO_URI']

mongo = PyMongo(app)


@app.route('/input_data/<sensor_id>/<value>')
def save_data(sensor_id, value):
    print(sensor_id, value)

    mongo.db.data.insert_one(
        {'sensor': sensor_id, 'value': value})

    return 200


@app.route('/get_devices')
def get_devices():
    devices_list = mongo.db.devices.find()
    return devices_list


@app.route('/get_data/<sensor_id>')
def get_data(sensor_id):
    data_list = mongo.db.data.find({'sensor': sensor_id})
    datas = [data for data in data_list]
    return str(datas)


if __name__ == '__main__':
    app.run(debug=True)
