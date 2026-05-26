from datetime import date
from app.extensions import db
from app.models.goal import Goal
from app.utils.validators import validate_goal_payload

def list_goals(user_id):
    return Goal.query.filter_by(user_id=user_id).order_by(Goal.created_at.desc()).all()

def create_goal(user_id, data):
    ok, message = validate_goal_payload(data)
    if not ok:
        return False, message

    goal = Goal(
        user_id=user_id,
        titulo=data["titulo"].strip(),
        descricao=(data.get("descricao") or "").strip() or None,
        valor_meta=float(data["valor_meta"]),
        valor_atual=float(data.get("valor_atual") or 0),
        prazo=date.fromisoformat(data["prazo"]),
        status=data.get("status", "ativa")
    )
    db.session.add(goal)
    db.session.commit()
    return True, goal

def update_goal(user_id, goal_id, data):
    goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
    if not goal:
        return False, "Meta não encontrada."

    if data.get("titulo"):
        goal.titulo = data["titulo"].strip()
    if data.get("descricao") is not None:
        goal.descricao = data["descricao"].strip() if data["descricao"] else None
    if data.get("valor_meta") not in (None, ""):
        goal.valor_meta = float(data["valor_meta"])
    if data.get("valor_atual") not in (None, ""):
        goal.valor_atual = float(data["valor_atual"])
    if data.get("prazo"):
        goal.prazo = date.fromisoformat(data["prazo"])
    if data.get("status"):
        goal.status = data["status"]

    db.session.commit()
    return True, goal

def delete_goal(user_id, goal_id):
    goal = Goal.query.filter_by(id=goal_id, user_id=user_id).first()
    if not goal:
        return False, "Meta não encontrada."
    db.session.delete(goal)
    db.session.commit()
    return True, None
