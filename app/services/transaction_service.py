from datetime import date
from app.extensions import db
from app.models.transaction import Transaction
from app.utils.validators import validate_transaction_payload

def list_transactions(user_id):
    return Transaction.query.filter_by(user_id=user_id).order_by(Transaction.data.desc(), Transaction.id.desc()).all()

def create_transaction(user_id, data):
    ok, message = validate_transaction_payload(data)
    if not ok:
        return False, message

    transaction = Transaction(
        user_id=user_id,
        tipo=data["tipo"],
        categoria=data["categoria"],
        valor=float(data["valor"]),
        descricao=(data.get("descricao") or "").strip() or None,
        data=date.fromisoformat(data.get("data")) if data.get("data") else date.today(),
    )
    db.session.add(transaction)
    db.session.commit()
    return True, transaction

def delete_transaction(user_id, transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id, user_id=user_id).first()
    if not transaction:
        return False, "Transação não encontrada."
    db.session.delete(transaction)
    db.session.commit()
    return True, None
