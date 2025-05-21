from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.login_controller import authenticate_user

bp = Blueprint('login', __name__)

@bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@bp.route('/login', methods=['POST'])
def process_login():
    email = request.form.get('email')
    password = request.form.get('password')
    if authenticate_user(email, password):
        return redirect(url_for('home.index'))
    else:
        return render_template('login.html', error='Invalid credentials')
