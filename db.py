from app import create_app, db

app = create_app()

def criar_banco():
    with app.app_context():
        db.create_all()
        print("✅ Banco de dados criado com sucesso!")

def dropar_banco():
    with app.app_context():
        db.drop_all()
        print("🗑️ Banco de dados apagado com sucesso!")

# Execução por linha de comando
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python db.py [criar|dropar]")
        exit()

    if sys.argv[1] == "criar":
        criar_banco()
    elif sys.argv[1] == "dropar":
        dropar_banco()
    else:
        print("Comando inválido. Use 'criar' ou 'dropar'.")
