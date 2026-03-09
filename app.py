from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    time.sleep(4)  # Pause de 4 secondes
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))  # Bind sur PORT Render [web:1]
