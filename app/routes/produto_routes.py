from flask import Blueprint, render_template
from app.controllers.produtos_controller import get_produtos

bp = Blueprint('produtos', __name__)

@bp.route('/produtos')
def listar_produtos():
    produtos = get_produtos()
    return render_template('index.html', produtos=produtos)
