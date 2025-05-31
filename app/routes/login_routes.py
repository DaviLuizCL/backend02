from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models.usuario import User

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@login_bp.route('/process', methods=['POST'])
def process_login():
    email = request.form['email']
    senha = request.form['senha']
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.senha, senha):
        login_user(user)
        flash("Login efetuado com sucesso!", "success")
        return redirect(url_for('home.index'))  # ou url_for('home.index') se for pra /produtos
    else:
        flash("Email ou senha incorretos", "danger")
        return redirect(url_for('login.login'))

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout efetuado com sucesso!")
    return redirect(url_for('login.login'))
