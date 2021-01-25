import flask
from flask import request, jsonify
from waitress import serve

app = flask.Flask(__name__)
app.config["DEBUG"] = True


demo_content = [
    #dictionary
    {'id' : 0,
    'keyA' : 'valueA',
    'keyB' : 'valueB'},
    {'id' : 1,
    'keyA' : 'valueC',
    'keyB' : 'valueD'},
    {'id' : 2,
    'keyA' : 'valueE',
    'keyB' : 'valueF'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Server-Client-App</h1><p>This site is a template API service.</p>"

#API URL http://127.0.0.1:5000/api/v1/resources/demo_content/all  
#shows all demo_content as a json result  
@app.route('/api/v1/resources/demo_content/all', methods=['GET'])
def api_all():
    return jsonify(demo_content)



if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)

