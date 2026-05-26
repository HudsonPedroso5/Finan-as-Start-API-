from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app.services.auth_service import register_user, authenticate_user, update_profile
from app.models.user import User

def register():
    data = request.get_json(silent=True) or {}
    ok, result = register_user(data)
    if not ok:
        return jsonify({"success": False, "message": result}), 400

    user = result
    token = create_access_token(identity=str(user.id))
    return jsonify({
        "success": True,
        "message": "Conta criada com sucesso.",
        "token": token,
        "user": user.to_dict()
    }), 201

def login():
    data = request.get_json(silent=True) or {}
    ok, result = authenticate_user(data)
    if not ok:
        return jsonify({"success": False, "message": result}), 401

    user = result
    token = create_access_token(identity=str(user.id))
    return jsonify({
        "success": True,
        "message": "Login realizado com sucesso.",
        "token": token,
        "user": user.to_dict()
    })

@jwt_required()
def me():
    user_id = int(get_jwt_identity())
    user = User.query.get_or_404(user_id)
    return jsonify({"success": True, "user": user.to_dict()})

@jwt_required()
def update_me():
    user_id = int(get_jwt_identity())
    user = User.query.get_or_404(user_id)
    data = request.get_json(silent=True) or {}
    user = update_profile(user, data)
    return jsonify({"success": True, "message": "Perfil atualizado.", "user": user.to_dict()})
