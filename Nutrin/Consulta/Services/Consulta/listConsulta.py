from Nutrin.Consulta.Services.Consulta.readConsulta import readConsulta

#listar todas as consultas == read
def listConsultas():
    status, dado = readConsulta()
    return dado

#listar por tipo estado


#listar por pagamento

#listar por horarios
def listOcupadoConsulta(id_ocupado):
    lista = listConsultas()
    consultas = []
    for c in lista:
        if c['horario_id'] == id_ocupado:
            consultas.append(c)
    return consultas

#listar por pacientes
def listPacienteConsulta(id_paciente):
    lista = listConsultas()
    consultas = []
    for c in lista:
        if c['paciente_id'] == id_paciente:
            consultas.append(c)
    return consultas


#listar tipoAtendimento