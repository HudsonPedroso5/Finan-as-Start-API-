from flask import Blueprint
from app.controllers.dashboard_controller import summary

dashboard_bp = Blueprint("dashboard_bp", __name__)

dashboard_bp.route("/summary", methods=["GET"])(summary)
