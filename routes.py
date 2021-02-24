from flask import Flask, request

from main import insertUsuario

app = Flask("Youtube")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola" : "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():

    body = request.get_json()

    if("nome" not in body):
        return geraResponse(400, "O parametro nome é obrigatório")

    if("email" not in body):
        return geraResponse(400, "O parametro email é obrigatório")

    if("senha" not in body):
        return geraResponse(400, "O parametro senha é obrigatório")
    
    if("telefone" not in body):
        return geraResponse(400, "O parametro telefone é obrigatório")

    usuario = insertUsuario(body["nome"], body["email"], body["senha"], body["telefone"])

    return geraResponse(200, "Usuario criado", "user", usuario)


def geraResponse(status, mensagem, nomeConteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nomeConteudo and conteudo):
        response[nomeConteudo] = conteudo

    return response

app.run()