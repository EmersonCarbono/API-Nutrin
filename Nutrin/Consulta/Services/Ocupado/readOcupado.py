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
                'id':ocup.id,
                'horaI': ocup.horaI,
                'horaF': ocup.horaF
            })
        return True, lista
    return False, 'Nenhum horario ocupado'

def readAllOcupado(f=False):
    ocupados = Ocupado.query.all()
    if ocupados != None:
        if f:
            return True, ocupados
        ocupados_dic = []
        for o in ocupados:
            ocupados_dic.append({
                'id': o.id,
                'horario_id': o.horario_id,
                'horaI': o.horaI,
                'horaF': o.horaF
            })
        return True, ocupados_dic
    return False, 'Nenhuma hora ocupada cadastrada'


