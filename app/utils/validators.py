def validate_email(email):
    return isinstance(email, str) and "@" in email and "." in email

def validate_password(password):
    return isinstance(password, str) and len(password) >= 6

def validate_required_fields(data, fields):
    missing = [field for field in fields if not data.get(field)]
    return missing

def validate_transaction_payload(data):
    missing = validate_required_fields(data, ["tipo", "categoria", "valor"])
    if missing:
        return False, f"Campos obrigatórios ausentes: {', '.join(missing)}"
    try:
        float(data["valor"])
    except (TypeError, ValueError):
        return False, "O valor da transação deve ser numérico."
    return True, ""

def validate_goal_payload(data):
    missing = validate_required_fields(data, ["titulo", "valor_meta", "prazo"])
    if missing:
        return False, f"Campos obrigatórios ausentes: {', '.join(missing)}"
    try:
        float(data["valor_meta"])
        if data.get("valor_atual") not in (None, ""):
            float(data["valor_atual"])
    except (TypeError, ValueError):
        return False, "Os valores da meta devem ser numéricos."
    return True, ""
