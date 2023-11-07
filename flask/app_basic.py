from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return f'Welcome to my Flask Endpoint :)'

@app.route('/pets', methods=['GET'])
def pets_get():
    number = request.args.get('number', '?')
    pet = request.args.get('pet', '?')
    return jsonify({'error': 'Invalid JSON'}), 400

@app.route('/feeling', methods=['GET'])
def feeling_get():
    emotion = request.args.get('emotion', 'nothing')
    return jsonify({'message': f'Why are you feeling {emotion}?'})

if __name__ == '__main__':
    app.run(debug=True)


## test CURL for post:
# curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d '{"name": "Cooper"}'

## test CURL for get:
# curl -X GET http://localhost:5000/hello?name=Cooper