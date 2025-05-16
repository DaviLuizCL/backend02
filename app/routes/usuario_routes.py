from flask import Blueprint
from app.controllers.usuario_controller import criar_usuario

bp = Blueprint('usuario_routes', __name__)

bp.route('/usuarios', methods=['POST'])(criar_usuario)
