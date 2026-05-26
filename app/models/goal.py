from datetime import datetime
from app.extensions import db

class Goal(db.Model):
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    valor_meta = db.Column(db.Numeric(10, 2), nullable=False)
    valor_atual = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    prazo = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(30), nullable=False, default="ativa")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    @property
    def progresso(self):
        try:
            if float(self.valor_meta or 0) == 0:
                return 0
            return min(100, round((float(self.valor_atual or 0) / float(self.valor_meta)) * 100, 1))
        except Exception:
            return 0

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "valor_meta": float(self.valor_meta),
            "valor_atual": float(self.valor_atual),
            "prazo": self.prazo.isoformat() if self.prazo else None,
            "status": self.status,
            "progresso": self.progresso,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
