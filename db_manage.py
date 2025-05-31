# db_manage.py

from app import create_app
from app.db import db
from app.models.usuario import User  # importa os models pra registrar no metadata
from flask import current_app

app = create_app()
app.app_context().push()

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        comando = sys.argv[1]

        if comando == 'dropar':
            print("🗑️ Dropar banco de dados...")
            db.drop_all()
        elif comando == 'criar':
            print("✅ Criando tabelas do banco de dados...")
            db.create_all()
        else:
            print("❌ Comando desconhecido. Use 'dropar' ou 'criar'.")
    else:
        print("❌ Nenhum comando fornecido. Use 'dropar' ou 'criar'.")
