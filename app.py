from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello from Flask"

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Handle file upload logic here
        file = request.files['file']
        # Process the file as needed
        print('file recieved')
        
        return jsonify('Files recieved Successfully')
    
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)  
