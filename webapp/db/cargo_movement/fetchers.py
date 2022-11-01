from webapp.db import CargoMovement
from webapp.db.cargo_movement.models import AttachmentCargoMovement


def get_movements():
    return CargoMovement.query.filter().all()


def get_movement_by_id(id: int):
    try:
        return CargoMovement.query.get(id)
    except (RuntimeError):
        return None


def get_attachments(movement_id: int):
    return AttachmentCargoMovement.query.filter(AttachmentCargoMovement.movement_id == movement_id).all()


def get_attachment_by_id(id: int):
    try:
        return AttachmentCargoMovement.query.get(id)
    except (RuntimeError):
        return None
