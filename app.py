from flask import Flask
import os
from config import Config
from models import db, Position  # Import de Position pour l'insertion automatique
from flask_migrate import Migrate
from flask_cors import CORS
from pythocode import main as main_blueprint
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db.init_app(app)
migrate = Migrate(app, db)

# Allow all origins
CORS(app, supports_credentials=True, origins="https://gestion-planning-git-gestion-planning-msouhail-khs-projects.vercel.app")

mail = Mail(app)

app.register_blueprint(main_blueprint)

# Création des tables et insertion automatique des positions
with app.app_context():
    db.create_all()

    # Vérifier si les données existent déjà pour éviter les doublons
    if Position.query.count() == 0:
        positions = [Position(id=i, name=f"Chaîne {i}") for i in range(1, 7)]
        db.session.add_all(positions)
        db.session.commit()
        print("✅ Données Position insérées avec succès !")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
