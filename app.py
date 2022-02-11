from flask import Flask
# set FLASK_ENV="development"

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
# app.run(host='0.0.0.0', port=5000, debug=True, Environment="development")


