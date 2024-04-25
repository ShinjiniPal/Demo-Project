from flask import Flask, request, jsonify
from utilsfl import Utils
app = Flask(__name__)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    data = request.get_json()
    operation = data.get('operation', '')
    result = Utils.calculate(operation)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run()