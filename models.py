
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# from app import db
# -------------------------------------------------------------------------------------------
#  Models
# -------------------------------------------------------------------------------------------

class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(
      db.DateTime,
      nullable=False,
    )

    # Venue
    venue = db.relationship('Venue')
    venue_id = db.Column(
      db.Integer,
      db.ForeignKey('venues.id', ondelete='CASCADE'),
      nullable=False,
    )

    # Artist
    artist = db.relationship('Artist')
    artist_id = db.Column(
      db.Integer,
      db.ForeignKey('artists.id', ondelete='CASCADE'),
      nullable=False,
    )


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show')
    artists = db.relationship(
        'Artist',
        secondary='shows',
        back_populates='venues'
    )


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show')
    venues = db.relationship(
        'Venue',
        secondary='shows',
        back_populates='artists'
    )
