from flask import Flask
app = Flask(__name__)


@app.route('/')
def mille():
    return 'mille'

if __name__ == '__main__':
    app.run()
