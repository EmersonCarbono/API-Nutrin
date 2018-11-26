import requests as Req

url_basica = 'http://127.0.0.1:5000'

def testeListarPaciente():
    url = url_basica + '/pacientes'
    dados = Req.api.get(url).json()
    return dados

def testeCadastrarPaciente():
    url = url_basica + '/paciente/cadastrar'
    paciente = {
        "username":'igao',
         "password":"45698",
         'nome':'igor ueredh',
         'email':'uehara@gmail.com',
         'celular':'41986452314',
         'dataNascimento':'1998-08-01',
         'sexo':"M",
         'cidade':'são paulo',
         'profissao':'Ator',
         'objetivo':'emagrecer',
         'altura': '1.80',         
    }
    paciente2 = {
        "username":'jackChien',
         "password":"chien",
         'nome':'chien',
         'email':'chiengraca@gmail.com',
         'celular':'11985632258',
         'dataNascimento':'1973-04-03',
         'sexo':"M",
         'cidade':'Rio de janeiro',
         'profissao':'Surfista',
         'objetivo':'hipertrofia',
         'altura': '1.75',         
    }
    dados = Req.api.post(url, json=paciente).json()
    return dados

def testePesquisarPaciente(username):
    url = url_basica + '/paciente/consultar/' + username
    dados = Req.api.get(url).json()
    return dados

def testeDesativarPaciente(username):
    url = url_basica + '/paciente/desativar/' + username
    dados = Req.api.get(url).json()
    return dados

def testeAtivarPaciente(username):
    url = url_basica + '/paciente/ativar/' + username
    dados = Req.api.get(url).json()
    return dados

def testeAlterarPaciente(username_atual, username, nome, email, celular, tipo, dataNascimento, sexo, cidade, profissao, objetivo, altura):
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
        "altura": altura
        
    }
    dados = Req.api.put(url, json=paciente).json()
    return dados

def main():
    #print(testeListarPaciente())
    print(testeCadastrarPaciente())
    #print(testePesquisarPaciente('ozob'))
    #print(testeCadastrarPaciente())
    #print(testePesquisarPaciente('ozob'))
    #print(testeExcluirPaciente("ozob"))
    #print(testeAlterarPaciente('emerson', 'emerson', 'emerson', 'sid@gmail.com', '11955554662', 'P','1998-08-01', 'm', 'são paulo', 'devs', 'ganhar massa', 1.7))
    #print(testePesquisarPaciente('ozob'))
    #print(testeDesativarPaciente("ozob"))
    #print(testeAtivarPaciente("ozob"))
    #print(testeAlterarPaciente('ozob', 'ozob', 'Emerson TKP', 'lala@gmail.com', '11955554662', 'P','01081998', 'm', 'são paulo', 'devs', 'ficar monstrao', '1.85'))

main()
