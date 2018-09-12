from Nutrin import db
from TipoRefeicao import TipoRefeicao
from Anamnese import Anamnese

class Refeicao(db.Model):
    __tablename__ = "refeicoes"

    id = db.Column(db.Integer, primary_Key=True)
    anamnese_id = db.Column(db.Integer, db.ForeignKey('anamneses.id'), nullable=False)
    tipoRefeicao_id = db.Column(db.Integer, db.ForeignKey('tipoRefeicoes.id'), nullable=False)
    horario = db.Column(db.TIME,,nullable=False)
    refeicao = db.Column(db.String(200),nullable=False)

    def __init__(self, tipoRefeicao_id, horario, refeicao):
        self.tipoRefeicao_id = tipoRefeicao_id
        self.horario = horario
        self.refeicao = refeicao
    
    def __repr__(self):
        return "<Refeição {} - {}>".format(self.tipoRefeicao_id, self.refeicao)

    #def __str__(self):