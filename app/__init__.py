from flask import Flask, jsonify, request, render_template
from app.config.config import Config
from app.extensions import db, migrate, jwt
from app.routes.auth_routes import auth_bp
from app.routes.transaction_routes import transaction_bp
from app.routes.goal_routes import goal_bp
from app.routes.dashboard_routes import dashboard_bp
from app.routes.education_routes import education_bp
from app.routes.web_routes import web_bp
from app.models import User, Transaction, Goal, EducationalContent

def seed_default_content():
    if EducationalContent.query.count() > 0:
        return

    contents = [
        EducationalContent(
            titulo="Organize seu orçamento",
            resumo="Aprenda a separar gastos fixos, variáveis e metas.",
            conteudo="Um orçamento simples ajuda a visualizar entradas e saídas e evita decisões impulsivas.",
            categoria="Orçamento",
            nivel="iniciante",
            duracao_minutos=5,
        ),
        EducationalContent(
            titulo="Diferença entre desejo e necessidade",
            resumo="Economizar começa com boas escolhas.",
            conteudo="Necessidades são essenciais; desejos podem ser planejados. Essa diferença melhora o controle financeiro.",
            categoria="Consumo consciente",
            nivel="iniciante",
            duracao_minutos=4,
        ),
        EducationalContent(
            titulo="Reserva de emergência",
            resumo="Tenha segurança para imprevistos.",
            conteudo="Guardar dinheiro para emergências evita dívidas e ajuda a manter estabilidade em momentos inesperados.",
            categoria="Planejamento",
            nivel="intermediario",
            duracao_minutos=6,
        ),
        EducationalContent(
            titulo="Meta financeira inteligente",
            resumo="Defina objetivos claros e mensuráveis.",
            conteudo="Metas funcionam melhor quando possuem valor, prazo e acompanhamento de progresso.",
            categoria="Metas",
            nivel="iniciante",
            duracao_minutos=5,
        ),
    ]
    db.session.add_all(contents)
    db.session.commit()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(web_bp)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(transaction_bp, url_prefix="/api/transactions")
    app.register_blueprint(goal_bp, url_prefix="/api/goals")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(education_bp, url_prefix="/api/education")

    with app.app_context():
        db.create_all()
        seed_default_content()

    @app.errorhandler(404)
    def not_found(error):
        if request.path.startswith("/api/"):
            return jsonify({"success": False, "message": "Recurso não encontrado."}), 404
        return render_template("error.html", code=404, message="Página não encontrada."), 404

    @app.errorhandler(400)
    def bad_request(error):
        if request.path.startswith("/api/"):
            return jsonify({"success": False, "message": "Requisição inválida."}), 400
        return render_template("error.html", code=400, message="Requisição inválida."), 400

    @app.errorhandler(401)
    def unauthorized(error):
        if request.path.startswith("/api/"):
            return jsonify({"success": False, "message": "Não autorizado."}), 401
        return render_template("error.html", code=401, message="Não autorizado."), 401

    @app.errorhandler(500)
    def internal_error(error):
        if request.path.startswith("/api/"):
            return jsonify({"success": False, "message": "Erro interno do servidor."}), 500
        return render_template("error.html", code=500, message="Erro interno do servidor."), 500

    return app
