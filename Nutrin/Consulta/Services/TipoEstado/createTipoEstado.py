from Nutrin.Consulta.Model.TipoEstado import TipoEstado
from Nutrin import db


def criarTipoEstado(nome):
    tipo_estado = TipoEstado(nome)
    db.session.add(tipo_estado)
    db.session.commit()
    return True, "Tipo estado cadastrado com sucesso"