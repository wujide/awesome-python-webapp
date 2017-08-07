# coding=utf-8
# __author__='wujide'

a = dict(one=1, two=2, three=3)
b = {'one': 11, 'two': 22, 'three': 33}
c = dict(zip(['one', 'two', 'three'], [111, 2222, 3333]))
d = dict((['three', 3], ['one', 1], ['two', 2]))
e = dict([['three', 3333], ['one', 1111], ['two', 2222]])
f = dict({'three': 3, 'one': 1, 'two': 2})

print a
print b
print c
print d
print e
print f

import json
from flask import Flask, jsonify

json.dumps(a)
print json.loads(json.dumps(a))
print json.loads(json.dumps(b))
print json.loads(json.dumps(c))
print json.loads(json.dumps(d))
print json.loads(json.dumps(e))
print json.loads(json.dumps(f))


app = Flask(__name__)


@app.route('/temp', methods=['get'])
def get_json():

    for data in [a, b, c, d, e]:
        print "get_json:", jsonify({'data': data})
        return jsonify({'data': data})
    # return jsonify({'data': json_data})
    # return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)



