from webapp.db import IssuanceOfCargo
from webapp.db.issuance_of_cargo.models import AttachmentIssuanceOfCargo


def get_issuances():
    return IssuanceOfCargo.query.filter().all()


def get_issuance_by_id(id: int):
    try:
        return IssuanceOfCargo.query.get(id)
    except (RuntimeError):
        return None


def get_attachments(issuance_id: int):
    return AttachmentIssuanceOfCargo.query.filter(AttachmentIssuanceOfCargo.issuance_id == issuance_id).all()


def get_attachment_by_id(id: int):
    try:
        return AttachmentIssuanceOfCargo.query.get(id)
    except (RuntimeError):
        return None
