from flask import Flask, render_template
import os

def start():

    app = Flask(__name__, static_url_path='/')

     # Use a non random key as long as the environment is explicitly set to development
    if os.getenv('FLASK_ENV') == 'development':
        app.secret_key = b'SUPERSECRETKEY'
        app.debug = True
    else:
        app.secret_key = os.urandom(24)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = start()
    app.run(debug=True)