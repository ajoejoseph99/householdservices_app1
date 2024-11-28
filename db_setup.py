from app import app, db
from models import User, Service, ServiceRequest

with app.app_context():
    db.create_all()
    print("Database initialized!")
