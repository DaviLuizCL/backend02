from flask import Blueprint, session, redirect, url_for, request, render_template, flash
import requests

carrinho_bp = Blueprint('carrinho', __name__, url_prefix='/carrinho')

@carrinho_bp.route('/adicionar', methods=['POST'])
def adicionar():
    produto_id = int(request.form['produto_id'])
    carrinho = session.get('carrinho', {})

    if str(produto_id) in carrinho:
        carrinho[str(produto_id)] += 1
    else:
        carrinho[str(produto_id)] = 1

    session['carrinho'] = carrinho
    return redirect(url_for('home.index'))

@carrinho_bp.route('/remover', methods=['POST'])
def remover():
    produto_id = str(request.form['produto_id'])
    carrinho = session.get('carrinho', {})

    if produto_id in carrinho:
        carrinho[produto_id] -= 1
        if carrinho[produto_id] <= 0:
            carrinho.pop(produto_id)

    session['carrinho'] = carrinho
    return redirect(url_for('home.index'))

@carrinho_bp.route('/cancelar', methods=['POST'])
def cancelar():
    produto_id = str(request.form['produto_id'])
    carrinho = session.get('carrinho', {})

    carrinho.pop(produto_id, None)
    session['carrinho'] = carrinho
    return redirect(url_for('home.index'))

@carrinho_bp.route('/')
def finalizar():
    carrinho = session.get('carrinho', {})
    produtos = []

    for produto_id, qtd in carrinho.items():
        resp = requests.get(f'https://dummyjson.com/products/{produto_id}')
        if resp.status_code == 200:
            produto = resp.json()
            produto['quantidade'] = qtd
            produtos.append(produto)

    return render_template('finalizar.html', produtos=produtos)

@carrinho_bp.route('/pagar', methods=['POST'])
def pagar():
    session.pop('carrinho', None)
    flash('Pagamento efetuado com sucesso!', 'success')
    return redirect(url_for('home.index'))
