from Nutrin import db
from Paciente import Paciente
from Nutrin.Consulta.Model.Consulta import Consulta
from Nutrin.Alimentacao.Model.Anamnese import Anamnese


class FichaPaciente(db.Model):
    __tablename__ = "fichaPacientes"

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id')) 
    altura = db.Column(db.Float, nullable=False)
    consultas = db.relationship('Consulta', backref='dadosConsulta')
    anamneses = db.relationship('Anamnese', backref='alimentacao')

    def __init__(self,paciente_id,altura):
        self.paciente_id = paciente_id
        self.altura = altura

    def __repr__(self):
        return "<Ficha do Paciente: {} - {}>".format(self.paciente_id,self.altura)
