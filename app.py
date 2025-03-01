from flask import Flask
import os
from config import Config
from models import db, Position  
from flask_migrate import Migrate
from flask_cors import CORS
from pythocode import main as main_blueprint
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

CORS(app, supports_credentials=True, origins="*")

mail = Mail(app)

app.register_blueprint(main_blueprint)

with app.app_context():
    db.create_all()

    if Position.query.count() == 0:
        positions = [Position(id=i, name=f"Chaîne {i}") for i in range(1, 7)]
        db.session.add_all(positions)
        db.session.commit()
        print("✅ Données Position insérées avec succès !")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

