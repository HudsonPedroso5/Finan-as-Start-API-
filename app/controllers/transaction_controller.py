from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services.transaction_service import list_transactions, create_transaction, delete_transaction

@jwt_required()
def get_transactions():
    user_id = int(get_jwt_identity())
    items = [tx.to_dict() for tx in list_transactions(user_id)]
    return jsonify({"success": True, "items": items})

@jwt_required()
def post_transaction():
    user_id = int(get_jwt_identity())
    data = request.get_json(silent=True) or {}
    ok, result = create_transaction(user_id, data)
    if not ok:
        return jsonify({"success": False, "message": result}), 400
    return jsonify({"success": True, "message": "Transação criada com sucesso.", "item": result.to_dict()}), 201

@jwt_required()
def remove_transaction(transaction_id):
    user_id = int(get_jwt_identity())
    ok, message = delete_transaction(user_id, transaction_id)
    if not ok:
        return jsonify({"success": False, "message": message}), 404
    return jsonify({"success": True, "message": "Transação removida."})
