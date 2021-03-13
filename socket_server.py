import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print('-------------------')
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('-------------------')
    print('disconnect ', sid)

@sio.on('newPrice')
def newPrice(sid, data):
    print(data)

eventlet.wsgi.server(eventlet.listen(('', 7777)), app)
