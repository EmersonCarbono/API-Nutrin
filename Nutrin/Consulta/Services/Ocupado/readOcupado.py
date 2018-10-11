from Nutrin import db
from Nutrin.Consulta.Model.Ocupado import Ocupado

def readOcupado(id,f=False):
    o = Ocupado.query().filter(id==id)
    if o != None:
        if f:
            return True, o
        return True, {
        id: o.id,
        data: o.horario_id, 
        hora: o.horaI,
        horaF: o.horaF }
    return False, "Esse id não foi encontrado"

def readOcupadoNoPeriodo(id_periodo):
    o = Ocupado.query().filter(horario_id == id_periodo)
    if o != None:
        lista = []
        for ocup in o:
            lista.append({
                'horaI': ocup.horaI,
                'horaF': ocup.horaF
            })
        return True, lista
    return False, 'Nenhum horario ocupado'
