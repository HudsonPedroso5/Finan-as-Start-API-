from flask import Blueprint
from app.controllers.education_controller import get_content

education_bp = Blueprint("education_bp", __name__)

education_bp.route("", methods=["GET"])(get_content)
