from flask import Flask, Response, request
from flask_cors import CORS
import argparse
import base64

# from read_stream import get_stream

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

users = {
    "admin": "admin",  # Basic YWRtaW46YWRtaW4=
}

tokens = {
    "admin": "admin"  # Bearer admin
}


@app.route('/')
def index():
    return "server online"


""" @app.route('/stream')
def http_stream():
    # /stream?url=<base64 url>
    userInput = request.args.get('url')
    if userInput == None:
        return Response(get_stream(0),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    url = base64.b64decode(userInput).decode('utf-8')
    if not url.strip():
        return Response('Missing parameters, eg. /stream?url=base64 url', status=400)

    return Response(get_stream(url),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
 """

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Video Server")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="Running on the given port")
    args: argparse.Namespace = parser.parse_args()
    app.run(host='0.0.0.0', debug=True, port=args.port)