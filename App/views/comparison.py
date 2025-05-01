from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize

comparison_views = Blueprint('comparison_views', __name__, template_folder='../templates')

@comparison_views.route('/comparison', methods=['GET'])
def comparison_page():
    return render_template('comparison.html')
