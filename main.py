from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    'mongodb://joao:joao@mongodb/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.5.0')

db = client["sensors"]

'''

@app.route("/add_one/<sensor_id>/<value>")
def add_one(sensor_id, value):
    print(sensor_id, value)
    collection = db["Student"]
    db.todos.insert_one({'sensor_id': sensor_id, 'value': value})
    return flask.jsonify(message="success")

'''


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {0}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
