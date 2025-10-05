from flask import Blueprint, render_template, redirect, url_for, session
from data import Data

home_bp = Blueprint('home', __name__, template_folder='template', static_folder='static', static_url_path='/home/static')

@home_bp.route('/')
def home():
    if session.get('id') != None:
        for user in Data:
            if user.get('id') == session.get('id'):
                return render_template('home.html', user_name = user.get('nome'))
    return redirect(url_for('auth.login_get'))