from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize

trend_views = Blueprint('trend_views', __name__, template_folder='../templates')

@trend_views.route('/trends', methods=['GET'])
def trend_page():
    return render_template('trends.html')
