from Nutrin.Paciente.Model.Paciente import Paciente
from Nutrin.User.Services.cadastrarUser import cadastrarUser
from Nutrin.User.Services.buscarUser import buscarUser
from Nutrin import db

from Nutrin.Controle.converter_data import stringToDate

def cadastrarPaciente(username, password, nome, email, celular, dataNascimento, sexo, cidade, profissao, objetivo, ativo):
    status, mensagem = cadastrarUser(username, password, nome, email, celular, "P", ativo)
    if status:
        dataNascimento = stringToDate(dataNascimento)
        user = buscarUser(username, True)
        id_user = user.id
        p = Paciente(id_user, dataNascimento, sexo, cidade, profissao, objetivo)
        db.session.add(p)
        db.session.commit()
        return True, 'Paciente cadastrado com sucesso'
    return status, mensagem