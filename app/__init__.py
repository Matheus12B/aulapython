from flask import Flask   # Importa Flask

app = Flask(__name__)   # Cria o blog

from app import routes  # Importa todas as rotas
