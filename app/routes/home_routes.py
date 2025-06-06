from flask import Blueprint, render_template, session
from app.controllers.produtos_controller import get_produtos

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    produtos = get_produtos()
    carrinho = session.get("carrinho", {})

    # Ordena: produtos no carrinho vão primeiro
    produtos.sort(key=lambda p: 0 if str(p["id"]) in carrinho else 1)

    return render_template('index.html', produtos=produtos)
