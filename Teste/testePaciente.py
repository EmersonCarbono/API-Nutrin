import requests as Req

url_basica = 'http://127.0.0.1:5000'

def testeListarPaciente():
    url = url_basica + '/pacientes'
    dados = Req.api.get(url).json()
    return dados

def testeCadastrarPaciente():
    url = url_basica + '/paciente/cadastrar'
    paciente = {
        "username":'emerson',
         "password":"0420",
         'nome':'Loki',
         'email':'sid@gmail.com',
         'celular':'11955554662',
         'dataNascimento':'1998-08-01',
         'sexo':"M",
         'cidade':'são paulo',
         'profissao':'programador',
         'objetivo':'emagrecer',
         'altura': '1.70',         
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
        'altura':altura
        
    }
    dados = Req.api.put(url, json=paciente).json()
    return dados

def main():
    #print(testeListarPaciente())
    #print(testeCadastrarPaciente())
    #print(testePesquisarPaciente('ozob'))
    #print(testeExcluirPaciente("ozob"))
    print(testeAlterarPaciente('emerson', 'emerson', 'emerson', 'sid@gmail.com', '11955554662', 'P','1998-08-01', 'm', 'são paulo', 'devs', 'ganhar massa', 1.7))

main()
