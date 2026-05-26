from flask import jsonify
from app.services.education_service import list_content

def get_content():
    items = [item.to_dict() for item in list_content()]
    return jsonify({"success": True, "items": items})
