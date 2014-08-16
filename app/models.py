from app import db
from flask_login import UserMixin

class Customer(db.Model):
  # A customer inside insync.io's database
  google_id = db.Column(db.String(255), primary_key=True)
  stripe_id = db.Column(db.String(255), unique=True)

  def __init__(self, google_id, stripe_id):
    self.google_id = google_id
    self.stripe_id = stripe_id

  def __repr__(self):
    return '<Customer %r>' % self.google_id