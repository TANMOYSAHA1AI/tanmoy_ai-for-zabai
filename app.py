from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    messages.append(data)
    emit('message', data, broadcast=True)

@socketio.on('get_messages')
def get_messages():
    emit('all_messages', messages)

if __name__ == '__main__':
    socketio.run(app, debug=True)