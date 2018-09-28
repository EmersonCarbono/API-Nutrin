from Nutrin import db

class Horarios(db.Model):
    __tablename__ = "horarios"
    __table_args__ = (
        db.UniqueConstraint('data', 'hora', name='horario unico'),
    )

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Datetime, nullable=False)
    hora = db.Column(db.TIME, nullable=False)
    utilizado = db.Column(db.Boolean, default=False)

    def __init__(self, data, hora):
        self.data = data
        self.hora = hora

    def __repr__(self):
        return "<Horários disponíveis: {} - {} - {}".format(self.data, self.hora, self.utilizado)

