from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import time
import chess.chess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + str(data))
    time.sleep(3)
    send(data, broadcast=True)

@socketio.on('test')
def handle_test_message(data):
    print('received test: ' + str(data))
    time.sleep(3)
    emit('test', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)