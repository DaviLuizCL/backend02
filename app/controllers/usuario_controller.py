from flask import request, jsonify
from app.models.usuario import Usuario
from app import db

def criar_usuario():
    dados = request.get_json()

    nome = dados.get('nome')
    email = dados.get('email')

    if not nome or not email:
        return jsonify({'erro': 'Nome e email são obrigatórios'}), 400

    novo_usuario = Usuario(nome=nome, email=email)
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({'mensagem': 'Usuário criado com sucesso!'}), 201
