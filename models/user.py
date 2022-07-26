from db import db
from models.enums import UserRoleModel


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class ComplainerModel(BaseUserModel):
    __tablename__ = 'complainers'

    role = db.Column(db.Enum(UserRoleModel), default=UserRoleModel.complainer, nullable= False)
    complaints = db.relationship("ComplaintModel", backref="complaint", lazy="dynamic")


class ApproverModel(BaseUserModel):
    __tablename__ = 'approvers'

    role = db.Column(db.Enum(UserRoleModel), default=UserRoleModel.approver, nullable= False)


class AdminModel(BaseUserModel):
    __tablename__ = 'admins'

    role = db.Column(db.Enum(UserRoleModel), default=UserRoleModel.admin, nullable= False)
