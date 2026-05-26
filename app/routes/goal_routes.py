from flask import Blueprint
from app.controllers.goal_controller import get_goals, post_goal, put_goal, remove_goal

goal_bp = Blueprint("goal_bp", __name__)

goal_bp.route("", methods=["GET"])(get_goals)
goal_bp.route("", methods=["POST"])(post_goal)
goal_bp.route("/<int:goal_id>", methods=["PUT"])(put_goal)
goal_bp.route("/<int:goal_id>", methods=["DELETE"])(remove_goal)
