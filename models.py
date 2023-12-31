"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_PHOTO_URL = 'https://cdn.vectorstock.com/i/preview-1x/65/30/\
    default-image-icon-missing-picture-page-vector-40546530.jpg'
def connect_db(app):
    """Connect this database to provided Flask app."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet (db.Model):
    """Pets up for adoption"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(
        db.Text,
        nullable=False)      # Should just be string / varchar

    species= db.Column(db.Text,                # fix indentation like for name
                       nullable=False)

    photo_url = db.Column(db.Text,
                          nullable=False,
                          default= DEFAULT_PHOTO_URL)

    age = db.Column(db.Text,
                    nullable=False)

    notes = db.Column(db.Text)  # We either have notes or not, so not nullable

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
