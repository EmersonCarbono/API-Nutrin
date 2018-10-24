import requests as Req

#from Nutrin.Controle.converter_data import *

url_basica = 'http://127.0.0.1:5000'

def testeCadastrarHorario():
    url = url_basica + '/horario/cadastrar'
    horario = {
        'data': '01112018',
        'horaI': '14:00',
        'horaF': '18:00'
    }
    Dados = Req.api.post(url, json=horario).json()
    return Dados

def testeAlterarHorario():
    url = url_basica + '/horario/alterar'
    horario = {
        'id':'1',
        'horaI':'14:00',
        'horaF': '17:00'
    }
    Dados = Req.api.put(url, json=horario).json()
    return Dados

def testeDeletarHorario(id_horario):
    url = url_basica + '/horario/deletar/' + id_horario
    Dados = Req.api.get(url).json()
    return Dados

def testeBuscarHorario():
    url = url_basica + '/horarios'
    Dados = Req.api.get(url).json()
    return Dados

def testeBuscarPorDia(horario_dia):
    url = url_basica + '/horarios' + horario_dia
    Dados = Req.api.get(url).json()
    return Dados

def testelistarHorarioDisp():
    url = url_basica + '/horarios/listaDisp'
    Dados = Req.api.get(url).json()
    return Dados

def main():
    print(testeCadastrarHorario())
    # print(testeAlterarHorario())
    # print(testeDeletarHorario('1'))
    #print(testeBuscarHorario())
    # print(testeBuscarPorDia('23102018'))
    # print(testelistarHorarioDisp())

main()