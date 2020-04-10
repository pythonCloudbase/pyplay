from flask_socketio import SocketIO 
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ashwin'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print("Received kindly.")

@socketio.on('my event')
def handle_my_custom_event(json,methods=['GET', 'POST']):
    print('recieved my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0' , port=5555, debug =True)

