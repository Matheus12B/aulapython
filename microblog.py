from flask import Flask   #Importa o Flask

app = Flask("microblog")    #Cria um blog


@app.route("/")      #Cria uma ligação com a função de baixo
def index():
    return 'Hello world'


app.run()   #Roda o blog
