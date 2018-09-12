from Nutrin import db
from TipoAtendimento import TipoAtendimento
from Antropometria import Antropometria
from TipoEstado import TipoEstado
from Nutrin.Paciente.Model.FichaPaciente import FichaPaciente

class Consulta(db.Model):
    __tablename__ = "consultas"

    id = db.Column(db.Integer, primary_key=True)
    fichaPaciente_id = db.Column(db.Integer, db.ForeignKey('fichaPacientes.id'), nullable=False)
    tipoAtendimento_id = db.Column(db.Integer, db.ForeignKey('tipoAtendimentos.id'), nullable=False)
    hora = db.Column(db.TIME, nullable=False)
    data = db.Column(db.Date, nullable=False)
    tipoEstado_id = db.Column(db.Integer, db.ForeignKey('tipoEstados.id'), nullable=False, default=1)
    antropometria_id = db.Column(db.Integer, db.ForeignKey('tipoAtendimentos.id'))
    dieta = db.Column(LargeBinary)
    pagamento = db.Column(Boolean)

    def __init__(self, fichaPaciente_id, tipoAtendimento_id, antropometria_id, tipoEstado_id, dieta):
        self.fichaPaciente_id = fichaPaciente_id
        self.tipoAtendimento_id = tipoAtendimento_id
        self.antropometria_id =antropometria_id
        self.tipoEstado_id = tipoEstado_id
        self.dieta = dieta

    def __repr__(self):
        return "<Consulta {}".format(self.tipoEstado_id)


    
