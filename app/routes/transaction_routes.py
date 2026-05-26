from flask import Blueprint
from app.controllers.transaction_controller import get_transactions, post_transaction, remove_transaction

transaction_bp = Blueprint("transaction_bp", __name__)

transaction_bp.route("", methods=["GET"])(get_transactions)
transaction_bp.route("", methods=["POST"])(post_transaction)
transaction_bp.route("/<int:transaction_id>", methods=["DELETE"])(remove_transaction)
