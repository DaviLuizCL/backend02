from flask import Blueprint, render_template
from app.controllers.produtos_controller import get_produtos
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    produtos = get_produtos()
    return render_template('index.html', produtos=produtos)
