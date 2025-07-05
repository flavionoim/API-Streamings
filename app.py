from flask import Flask, jsonify, request

app = Flask(__name__)

streamings = [
    {
        'id': 1, 
        'nome': 'The Office',
        'classificacao': '14+',
        'nota': '4.9'
    },
    {
        'id': 2, 
        'nome': 'Hunter x Hunter',
        'classificacao': '14+',
        'nota': '4.8'
    },
    {
        'id': 3, 
        'nome': 'The Flash',
        'classificacao': '12+',
        'nota': '4.9'
    },
    {
        'id': 4, 
        'nome': 'Lost',
        'classificacao': '16+',
        'nota': '4.7'
    },
    {
        'id': 5, 
        'nome': 'Bruxa de Blair',
        'classificacao': '14+',
        'nota': '5'
    },
    {
        'id': 6, 
        'nome': 'Bruxa de Blair 2',
        'classificacao': '14+',
        'nota': '4.6'
    },
    {
        'id': 7, 
        'nome': 'O Show de Truman',
        'classificacao': '12+',
        'nota': '4.9'
    },
    {
        'id': 8, 
        'nome': 'Clube da Luta',
        'classificacao': '18+',
        'nota': '4.9'
    },
    {
        'id': 9, 
        'nome': 'Ilha do Medo',
        'classificacao': '16+',
        'nota': '5'
    },
    {
        'id': 10, 
        'nome': 'Jurassic Park I',
        'classificacao': '12+',
        'nota': '5'
    },
    {
        'id': 11, 
        'nome': 'Jurassic Park II',
        'classificacao': '12+',
        'nota': '4.8'
    },
    {
        'id': 12, 
        'nome': 'Jurassic Park III',
        'classificacao': '12+',
        'nota': '4.6'
    },
    {
        'id': 13, 
        'nome': 'Jurassic World I',
        'classificacao': '12+',
        'nota': '5'
    },
    {
        'id': 14, 
        'nome': 'Jurassic World II',
        'classificacao': '12+',
        'nota': '4.7'
    },
    {
        'id': 15, 
        'nome': 'Jurassic World III',
        'classificacao': '12+',
        'nota': '5'
    },
    {
        'id': 16, 
        'nome': 'Jurassic World Rebirth',
        'classificacao': '12+',
        'nota': '4.9'
    },
]


#Consultar Filmes ou Séries Cadastradas
@app.route('/streamings',methods=['GET'])
def obter_filmes():
    return jsonify(streamings)


#Consultar Filmes ou Séries por Nome ( Como Pesquisar no Postman: http://localhost:5000/streamings/nome/The%20Office)
@app.route('/streamings/nome/<string:nome>', methods=['GET'])
def obter_streaming_por_nome(nome):
    for streaming in streamings:
        if streaming.get('nome').lower() == nome.lower():
            return jsonify(streaming)
    return jsonify({'erro': 'Filme/Série não encontrado'}), 404
       

#Consultar Filme ou Série (Id)
@app.route('/streamings/<int:id>', methods=['GET'])
def obter_streaming_por_id(id):
    for streaming in streamings:    
        if streaming.get('id') == id:
            return jsonify(streaming)

#Adicionar Novo Filme ou Série
@app.route('/streamings', methods = ['POST'])
def incluir_novo_filme():
    novo_filme = request.get_json()
    streamings.append(novo_filme)

    return jsonify(
        mensagem = 'Novo Filme/Série Cadastrado!',
        alunos = novo_filme) 

#Editar Filme ou Série
@app.route('/streamings/<int:id>', methods = ['PUT'])
def editar_filme(id):
    filme_editado = request.get_json()
    for indice,streaming in enumerate(streamings):
        if streaming.get('id') == id:
            streamings [indice].update(filme_editado)
            return jsonify(streamings[indice])

#Excluir Filme ou Série
@app.route('/streamings/<int:id>', methods = ['DELETE'])
def excluir_filme(id):
    for indice,streaming in enumerate(streamings):
        if streaming.get('id') == id:
            del streamings [indice]

            return jsonify(streamings)
        

#Total de Filmes e Séries
@app.route('/streamings/quantidade', methods=['GET'])
def contar_filmes():
    total = len(streamings)
    return jsonify({'mensagem': f'Atualmente há {total} filme(s) cadastrado(s).'})


#Pedir um Filme ou Série Aleatório para o Programa
import random

@app.route('/streamings/aleatorio', methods=['GET'])
def filme_aleatorio():
    return jsonify(random.choice(streamings))



app.run(port=5000,host='localhost',debug=True)