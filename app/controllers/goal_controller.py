from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services.goal_service import list_goals, create_goal, update_goal, delete_goal

@jwt_required()
def get_goals():
    user_id = int(get_jwt_identity())
    items = [goal.to_dict() for goal in list_goals(user_id)]
    return jsonify({"success": True, "items": items})

@jwt_required()
def post_goal():
    user_id = int(get_jwt_identity())
    data = request.get_json(silent=True) or {}
    ok, result = create_goal(user_id, data)
    if not ok:
        return jsonify({"success": False, "message": result}), 400
    return jsonify({"success": True, "message": "Meta criada com sucesso.", "item": result.to_dict()}), 201

@jwt_required()
def put_goal(goal_id):
    user_id = int(get_jwt_identity())
    data = request.get_json(silent=True) or {}
    ok, result = update_goal(user_id, goal_id, data)
    if not ok:
        return jsonify({"success": False, "message": result}), 404
    return jsonify({"success": True, "message": "Meta atualizada.", "item": result.to_dict()})

@jwt_required()
def remove_goal(goal_id):
    user_id = int(get_jwt_identity())
    ok, message = delete_goal(user_id, goal_id)
    if not ok:
        return jsonify({"success": False, "message": message}), 404
    return jsonify({"success": True, "message": "Meta removida."})
