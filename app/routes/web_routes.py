from flask import Blueprint, render_template

web_bp = Blueprint("web_bp", __name__)

@web_bp.route("/")
def home():
    return render_template("index.html")

@web_bp.route("/login")
def login_page():
    return render_template("login.html")

@web_bp.route("/signup")
def signup_page():
    return render_template("signup.html")

@web_bp.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

@web_bp.route("/transactions")
def transactions_page():
    return render_template("transactions.html")

@web_bp.route("/goals")
def goals_page():
    return render_template("goals.html")

@web_bp.route("/profile")
def profile_page():
    return render_template("profile.html")

@web_bp.route("/learn")
def learn_page():
    return render_template("learn.html")
