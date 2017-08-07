# coding=utf-8
# __author__='Administrator'

from flask import Flask, jsonify
import json

app = Flask(__name__)
data = {"name": "Tacey", "age": 13, "sex": "male", "interst": ("Programing", "Reading")}

# json.dumps
json_data = json.dumps(data)
print json_data
# json.loads
name = json.loads(json_data)['name']
print name


@app.route('/jsonify', methods=['get'])
def get_json():
    # return jsonify({'data': data})
    # return jsonify({'data': json_data})
    # return jsonify(data)
    json_data_get = json.dumps(data)
    print json_data_get
    return json_data_get


if __name__ == '__main__':
    app.run(debug=True)

