from sqlalchemy import func
from app.models.transaction import Transaction
from app.models.goal import Goal
from app.models.educational_content import EducationalContent

def get_dashboard_summary(user_id):
    receitas = Transaction.query.filter_by(user_id=user_id, tipo="receita").with_entities(
        func.coalesce(func.sum(Transaction.valor), 0)
    ).scalar() or 0

    despesas = Transaction.query.filter_by(user_id=user_id, tipo="despesa").with_entities(
        func.coalesce(func.sum(Transaction.valor), 0)
    ).scalar() or 0

    saldo = float(receitas) - float(despesas)

    recent_transactions = Transaction.query.filter_by(user_id=user_id).order_by(
        Transaction.data.desc(), Transaction.id.desc()
    ).limit(5).all()

    goals = Goal.query.filter_by(user_id=user_id).order_by(Goal.created_at.desc()).limit(4).all()
    contents = EducationalContent.query.order_by(EducationalContent.created_at.desc()).limit(4).all()

    return {
        "receitas": float(receitas),
        "despesas": float(despesas),
        "saldo": saldo,
        "recent_transactions": [item.to_dict() for item in recent_transactions],
        "goals": [item.to_dict() for item in goals],
        "educational_contents": [item.to_dict() for item in contents],
    }
