from Nutrin.Consulta.Services.Antropometria.readAntropometria import readAntropometria
from Nutrin import db

def deleteAntropometria(id_antropometria):
    a = readAntropometria(id_antropometria,True)
    if a:
        db.session.delete(a)
        db.session.commit()
        return True, "Deletado com sucesso"
    return False, "Antropometria não emcontrada"