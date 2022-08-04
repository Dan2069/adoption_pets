from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Returns image for pets"""

        return self.photo_url or GENERIC_IMAGE

def connect_db(app):
    """Conencts this database to provided Flask app.
    
    This should call this in the Flask app."""

    db.app = app
    db.init_app(app)