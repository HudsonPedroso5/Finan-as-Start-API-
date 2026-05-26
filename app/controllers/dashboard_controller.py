from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services.dashboard_service import get_dashboard_summary

@jwt_required()
def summary():
    user_id = int(get_jwt_identity())
    return jsonify({"success": True, "summary": get_dashboard_summary(user_id)})
