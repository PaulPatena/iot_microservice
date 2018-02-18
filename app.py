from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/buttonPressed', methods=['POST'])
def button_pressed_handler():

    device_id = request.args.get('deviceID')
    s = 'Server received msg {}'.format(device_id)
    print s
    return s


app.run(port=5010)
