from flask import Blueprint
from app.controllers.auth_controller import register, login, me, update_me

auth_bp = Blueprint("auth_bp", __name__)

auth_bp.route("/register", methods=["POST"])(register)
auth_bp.route("/login", methods=["POST"])(login)
auth_bp.route("/me", methods=["GET"])(me)
auth_bp.route("/me", methods=["PUT"])(update_me)
