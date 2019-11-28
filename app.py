import os
import math
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/hello')
def hello():
    version = os.environ.get('SERVICE_VERSION')

    # do some cpu intensive computation
    x = 0.0001
    for i in range(0, 1000000):
        x = x + math.sqrt(x)
    return render_template("home.html")


@app.route('/health')
def health():
    return 'Helloworld is healthy', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)
