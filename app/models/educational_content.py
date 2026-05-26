from datetime import datetime
from app.extensions import db

class EducationalContent(db.Model):
    __tablename__ = "educational_contents"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(140), nullable=False)
    resumo = db.Column(db.String(255), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    nivel = db.Column(db.String(30), nullable=False, default="iniciante")
    duracao_minutos = db.Column(db.Integer, nullable=False, default=5)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "resumo": self.resumo,
            "conteudo": self.conteudo,
            "categoria": self.categoria,
            "nivel": self.nivel,
            "duracao_minutos": self.duracao_minutos,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
