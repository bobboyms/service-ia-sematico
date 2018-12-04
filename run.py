import spacy

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.from_object('config')

nlp = spacy.load('pt_core_news_sm')

@app.route("/calcular_similaridade/",  methods=['POST','GET'])
def calcularSimilaridade():
    
    chave = request.args.get('chave')
    valor = request.args.get('valor')
    
    print(valor)
    
    doc_chave = nlp(chave)
    doc_texto = nlp(valor)
    
    similaridade = doc_chave.similarity(doc_texto)
    
    return jsonify({'chave' : chave, 'valor' : valor, 'similaridade' : similaridade})

@app.route("/calcular_similaridade/varios/",  methods=['POST','GET'])
def calcularSimilaridadeVarios():
    
    chave = request.args.get('chave')
    valor = request.args.get('valor')
    
    doc_chave = nlp(chave)
    valores = valor.split(",")

    lista =[]
    for valor in valores:
        if len(valor) > 0:
            doc_palavra = nlp(valor)
            sm = doc_chave.similarity(doc_palavra)
            lista.append({'chave' : chave, 'valor' : valor, 'similaridade' : sm})
    
    print(lista)
    
    return jsonify(lista)
     
if __name__ == "__main__":
    print("INICIANDO SERVI�O REST")
    app.run()