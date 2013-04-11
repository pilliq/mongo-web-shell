from flask import Flask
app = Flask(__name__, static_url_path='/static', static_folder='../frontend')

HOST = '0.0.0.0'
PORT = 8080
DEBUG = True

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
