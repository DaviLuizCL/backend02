# 🛠️ Projeto Backend com Flask + SQLAlchemy + Docker

Este projeto é um backend construído com **Flask** utilizando a arquitetura **MVC**, com banco de dados estruturado via **SQLAlchemy** e gerenciamento de containers com **Docker**. Também conta com um **Makefile** para facilitar o uso de comandos no dia a dia.

---

## 🚀 Tecnologias utilizadas

- 🐍 [Python 3.11+](https://www.python.org/)
- 🔥 [Flask](https://flask.palletsprojects.com/)
- 🧱 [SQLAlchemy](https://www.sqlalchemy.org/)
- 🐳 [Docker](https://www.docker.com/)
- ⚙️ [Docker Compose](https://docs.docker.com/compose/)
- 📁 SQLite (banco local de desenvolvimento)
- 🧪 Make (automação de comandos)

---

## 📦 Instalação e execução local

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/DaviLuizCL/backend02.git
cd backend02
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate.bat  # Windows (cmd)
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Crie o banco de dados

```bash
make reboot_db
```

Esse comando vai:
- Dropar o banco de dados (se já existir)
- Criar as tabelas com base nos modelos

### 5️⃣ Rode a aplicação local

```bash
make up
```

O servidor estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Executando com Docker

### Build e execução com Nginx (modo deploy):

```bash
make deploy
```

> Isso gera a imagem Docker e sobe os containers via `docker-compose`.

---

## 📋 Outros comandos úteis

```bash
make logs        # Visualiza logs em tempo real do container web
make reboot_db   # Dropa e recria o banco de dados local
```

---

## 🧠 Organização do projeto (MVC)

```
.
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── controllers/
│   └── routes/
├── db.py
├── run.py
├── config.py
├── Makefile
├── requirements.txt
└── docker-compose.yml
```

---

## 🤝 Contribuição
- [Fernando França](https://github.com/FernandoFrancaFilho)
- [Olenildo Filho](https://github.com/OlenildoFIlho)
- [Davi Luiz](https://github.com/DaviLuizCL)


---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
