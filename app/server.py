from flask import Flask
from flask import request, Response
import sys

app = Flask(__name__)
#port = sys.argv[1:]


@app.route("/hc")
def hc():
    return Response("Status: OK", 200)

@app.route("/")
def home():
    msg = request.args.get('msg')
    return Response(msg, 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

