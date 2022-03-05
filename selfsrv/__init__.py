from flask import Flask

def start():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World!'

    return app

if __name__ == '__main__':
    app.run(debug=True)