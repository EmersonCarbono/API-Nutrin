from Nutrin import db
from Nutrin.Consulta.Model.Horarios import Horarios

def listHorario():
    horarios = Horarios.query.all()
    lista = []
    for h in horarios:
        lista.appen({
        'hora_id' = h.id,
        'data' = h.data,
        'horaInicio' = h.horaInicio,
        'horaFim' = h.horaFim})
    return lista

def listHorarioData(data):
    horarios = Horarios.query.filter(data==data)
    lista = []
    for h in horarios:
        lista.appen({
        'hora_id' = h.id,
        'data' = h.data,
        'horaInicio' = h.horaInicio,
        'horaFim' = h.horaFim})
    return lista

def listHorarioDisp():
    from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo
    horarios = Horarios.query.all()
    disponiveis = []
    parcial = []
    for h in horarios:
        status, dado = readOcupadoNoPeriodo(h.id)
        if status:
            if dado
        else:
            disponiveis.append(h)



'''
listaTodos = listHorario()
    horarios = []
    for p in listaTodos:
        if data == p.data:
            horarios.append(p)
    
'''