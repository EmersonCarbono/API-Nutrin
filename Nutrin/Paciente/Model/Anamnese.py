from Nutrin import db
from Nutrin.Paciente.Model.Paciente import Paciente

class Anamnese(db.Model):
    __tablename__ = "anamneses"

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    dataNascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String(1))
    cidade = db.Column(db.String(50))
    profissao = db.Column(db.String(50))
    objetivo = db.Column(db.String(50))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, id_user, dataNascimento, sexo, cidade, profissao, objetivo):
        self.user_id = id_user
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.cidade = cidade
        self.profissao = profissao
        self.objetivo = objetivo
    
    def __repr__(self):
        return "<Paciente {0}>".format(self.user.username)
        