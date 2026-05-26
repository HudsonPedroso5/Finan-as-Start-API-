from datetime import datetime

def money(value):
    try:
        value = float(value or 0)
    except (TypeError, ValueError):
        value = 0
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def parse_date(value):
    if not value:
        return None
    if isinstance(value, datetime):
        return value
    return datetime.strptime(value, "%Y-%m-%d")
