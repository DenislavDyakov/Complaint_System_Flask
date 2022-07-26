# first we import built-in packages, then pip packages and lastly our own packages
from sqlalchemy import func

from db import db
from models.enums import ComplaintStatusModel


class ComplaintModel(db.Model):
    __tablename__ = 'complaint'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    create_on = db.Column(db.DateTime, server_default=func.now())
    status = db.Column(db.Enum(ComplaintStatusModel), default=ComplaintStatusModel.pending, nullable=False)
    complainer_id = db.Column(db.Integer, db.ForeignKey("complainers.id"))
    complainer = db.relationship("ComplainerModel")
