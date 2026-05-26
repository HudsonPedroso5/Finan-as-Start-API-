from datetime import datetime, date
from app.extensions import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    tipo = db.Column(db.String(20), nullable=False)  # receita | despesa
    categoria = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    data = db.Column(db.Date, nullable=False, default=date.today)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "tipo": self.tipo,
            "categoria": self.categoria,
            "valor": float(self.valor),
            "descricao": self.descricao,
            "data": self.data.isoformat() if self.data else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
