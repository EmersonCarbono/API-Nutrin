import requests as Req

url_basica = 'http://127.0.0.1:5000'

def testeConsultaCreate(paciente_id, tipoAtendimento_id, hora, data, tipoEstado_id):
    url = url_basica + '/consulta/cadastrar'
    consulta = {
        'paciente_id': paciente_id,
        'tipoAtendimento_id': tipoAtendimento_id,
        'hora': hora,
        'data': data,
        'tipoEstado_id': tipoEstado_id
    }
    dados = Req.api.get(url, json=consulta).json()
    return dados

def main():
    print(testeConsultaCreate(paciente_id, tipoAtendimento_id, hora, data, tipoEstado_id))

main()