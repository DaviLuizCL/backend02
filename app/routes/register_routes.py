from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.usuario_controller import criar_usuario

bp = Blueprint('register', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def process_register():
    if request.method == 'GET':
        return render_template('register.html')  # ou 'cadastro.html' se for esse o nome

    # POST: processa os dados do formulário
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirmar = request.form.get('confirmar_senha')

    if senha != confirmar:
        return render_template('register.html', error="As senhas não coincidem.")

    print(f"Novo usuário: {nome} - {email}")  # substitua depois pela lógica de salvar no banco

    return redirect(url_for('login.login'))


