import requests as Req

url_basica = 'http://127.0.0.1:5000'

def testeListarPaciente():
    url = url_basica + '/pacientes'
    dados = Req.api.get(url).json()
    return dados

def testeCadastrarPaciente():
    url = url_basica + '/paciente/cadastrar'
    paciente = {
        "username":'ozob',
         "password":"0123456",
         'nome':'Ozob bozo',
         'email':'ozob@gmail.com',
         'celular':'11955554662',
         'dataNascimento':'01081998',
         'sexo':"M",
         'cidade':'são paulo',
         'profissao':'programador',
         'objetivo':'emagrecer'
    }
    dados = Req.api.post(url, json=paciente).json()
    return dados

def testePesquisarPaciente(username):
    url = url_basica + '/paciente/consultar/' + username
    dados = Req.api.get(url).json()
    return dados

def testeExcluirPaciente(username):
    url = url_basica + '/paciente/excluir/' + username
    dados = Req.api.get(url).json()
    return dados

def testeAlterarPaciente(username_atual, username, nome, email, celular, tipo, dataNascimento, sexo, cidade, profissao, objetivo):
    url = url_basica + '/paciente/alterar-paciente'
    paciente = {
        "username_atual": username_atual,
        "username": username ,
        "nome": nome,
        "email": email,
        "celular": celular,
        "tipo": tipo,
        "dataNascimento": dataNascimento,
        "sexo": sexo,
        "cidade": cidade,
        "profissao": profissao,
        "objetivo": objetivo,
    }
    dados = Req.api.put(url, json=paciente).json()
    return dados

def main():
    #print(testeListarPaciente())
    #print(testeCadastrarPaciente())
    #print(testePesquisarPaciente('amanada'))
    #print(testeExcluirPaciente("emersoncarbono"))
    print(testeAlterarPaciente('TKPIG', 'ozob', 'Emerson TKP', 'teste@gmail.com', '11955554662', 'P','05092005', 'm', 'são paulo', 'devs', 'ganhar massa'))

main()
