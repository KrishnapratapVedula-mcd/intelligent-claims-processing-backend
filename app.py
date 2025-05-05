from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    response = {
        'key1': 'value1',
        'key2': 'value2'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
