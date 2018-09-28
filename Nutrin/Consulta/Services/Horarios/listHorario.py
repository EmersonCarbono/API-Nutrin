from Nutrin import db
from Nutrin.Consulta.Services.Horarios.readHorario import readHorario
from Nutrin.Consulta.Model.Horarios import Horarios

def listHorario():
    horarios = Horarios.query.all()
    lista = []
    for h in horarios:
        lista.appen({
        'hora_id' = h.id,
        'data' = h.data,
        'hora' = h.hora,
        'utilizado' = h.utilizado})
    return lista
    
