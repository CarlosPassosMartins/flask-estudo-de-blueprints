from flask import Flask
from auth.routes import auth_bp
from home.routes import home_bp
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


app.register_blueprint(auth_bp)
app.register_blueprint(home_bp, url_prefix='/home')

if __name__ == '__main__':
    app.run(debug=True)