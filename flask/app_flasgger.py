from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    return f'Welcome to my Flask Endpoint :)'

@app.route('/feeling', methods=['GET'])
def feeling_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: emotion
        in: query
        type: string
        required: false
        default: nothing
    responses:
      200:
        description: A greeting message
    """
    emotion = request.args.get('emotion', 'nothing')
    return f'Why are you feeling {emotion}?'

@app.route('/feeling', methods=['POST'])
def feeling_post():
    """
    This endpoint returns a question based on the name provided in the JSON body.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          required:
            - name
          properties:
            name:
              type: string
              default: nothing
    responses:
      200:
        description: A greeting message
      400:
        description: Invalid JSON
    """
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    emotion = data.get('emotion', 'nothing')
    return jsonify({'message': f'Why are you feeling {emotion}?'})

if __name__ == '__main__':
    app.run(debug=True)