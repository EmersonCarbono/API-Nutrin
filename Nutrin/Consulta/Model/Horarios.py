from Nutrin import db

class Horarios(db.Model):
    __tablename__ = "horarios"
    __table_args__ = (
        db.UniqueConstraint('data', 'horaInicio', 'horaFim', name='periodo unico'),
    )

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Datetime, nullable=False)
    horaInicio = db.Column(db.TIME, nullable=False)
    horaFim = db.Column(db.TIME, nullable=False)

    def __init__(self, data, horaInicio, horaFim):
        self.data = data
        self.horaIncio = horaInicio
        self.horaFim = horaFim

    def __repr__(self):
        return "<Período disponível: {} - {} - {}".format(self.data, self.horaInicio, self.horaFim)

