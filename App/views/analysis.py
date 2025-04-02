from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize

analysis_views = Blueprint('analysis_views', __name__, template_folder='../templates')

@analysis_views.route('/analysis', methods=['GET'])
def analysis_page():
    return render_template('analysis.html')
