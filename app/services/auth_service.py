from app.extensions import db
from app.models.user import User
from app.utils.validators import validate_email, validate_password

def register_user(data):
    nome = (data.get("nome") or "").strip()
    email = (data.get("email") or "").strip().lower()
    senha = data.get("senha") or ""

    if not nome:
        return False, "Informe o nome."
    if not validate_email(email):
        return False, "E-mail inválido."
    if not validate_password(senha):
        return False, "A senha precisa ter pelo menos 6 caracteres."

    if User.query.filter_by(email=email).first():
        return False, "Já existe uma conta com este e-mail."

    user = User(nome=nome, email=email)
    user.set_password(senha)

    db.session.add(user)
    db.session.commit()
    return True, user

def authenticate_user(data):
    email = (data.get("email") or "").strip().lower()
    senha = data.get("senha") or ""

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(senha):
        return False, "Credenciais inválidas."

    return True, user

def update_profile(user, data):
    nome = (data.get("nome") or "").strip()
    avatar = (data.get("avatar") or "").strip()

    if nome:
        user.nome = nome
    if avatar:
        user.avatar = avatar

    db.session.commit()
    return user
