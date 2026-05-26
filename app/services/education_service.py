from app.models.educational_content import EducationalContent

def list_content():
    return EducationalContent.query.order_by(EducationalContent.created_at.desc()).all()
