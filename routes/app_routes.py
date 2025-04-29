from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient


app_bp = Blueprint('app', __name__, template_folder='../templates')

client = MongoClient("mongodb://localhost:27017/")
db = client['app']
roles = db['roles']

@app_bp.route('/')
def home():
    all_app = roles.find()
    return render_template('index.html', roles=all_app)

@app_bp.route('/training')
def training():
    all_app = roles.find()
    return render_template('training.html', roles=all_app)
@app_bp.route('/resume')
def resume():
    return render_template('resume.html')

@app_bp.route('/getPath/<role_name>')
def getPath(role_name):
    """
    Handles requests for individual role pages (e.g., /path/Frontend).
    """
    try:
        # Fetch the role data from the database based on the role_name
        role_data = roles.find_one({'skill': role_name})  # Find the document by skill

        if role_data:
            role_data['_id'] = str(role_data['_id']) #convert object id to string
            # Render the template with the role data
            return render_template('role.html', path=role_data)
        else:
            return "Role not found", 404
    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        return jsonify({'error': error_message}), 500        # Fetch the role data from the database based on the role_name
