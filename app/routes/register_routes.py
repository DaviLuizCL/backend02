from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app import db
from app.models.usuario import User

register_bp = Blueprint('register', __name__, url_prefix='/register')

@register_bp.route('/', methods=['GET'])
def register():
    return render_template('register.html')

@register_bp.route('/process', methods=['POST'])
def process_register():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

    if senha != confirmar_senha:
        flash("Senhas não conferem")
        return redirect(url_for('register.register'))

    user_exists = User.query.filter_by(email=email).first()
    if user_exists:
        flash("Email já cadastrado")
        return redirect(url_for('register.register'))

    senha_hash = generate_password_hash(senha)
    novo_usuario = User(nome=nome, email=email, senha=senha_hash)

    db.session.add(novo_usuario)
    db.session.commit()

    flash("Conta criada com sucesso! Faça login para continuar.", "success")
    return redirect(url_for('login.login'))  # Redireciona para a tela de login

    return redirect(url_for('login.login'))
