from flask import Flask, redirect, request, render_template

app = Flask(__name__)

def leitura_jogo():
    posicoes = []
    for i in range (1,10):
        id = 'cel_'+str(i)
        cel = request.form[id]
        posicoes.append(cel)
    return posicoes


########### Rotas ##############
@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/fim_turno', methods=['POST'])
def passar_rodada():
    lista = leitura_jogo()    
    return render_template('teste.html', lista=lista)



app.run(debug=True)