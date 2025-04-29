from flask import Flask
from pymongo import MongoClient
from routes.app_routes import app_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

client = MongoClient(app.config['MONGO_URI'])
db = client['app']

app.register_blueprint(app_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

