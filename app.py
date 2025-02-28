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

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
CORS(app, supports_credentials=True, origins="https://gestion-planning-git-gestion-planning-msouhail-khs-projects.vercel.app")
mail = Mail(app)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.before_first_request
def initialize_database():
    if Position.query.count() == 0:
        positions = [Position(id=i, name=f"Chaîne {i}") for i in range(1, 7)]
        db.session.bulk_save_objects(positions)
        db.session.commit()
        print("✅ Données Position insérées avec succès !")

# Register blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
