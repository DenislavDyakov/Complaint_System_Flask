from enum import Enum


class UserRoleModel(Enum):
    complainer = "Complainer"
    approver = "Approver"
    admin = "Admin"


class ComplaintStatusModel(Enum):
    pending = "Waiting for Approval"
    approved = "Approved"
    rejected = "Rejected"
