from webapp.db import CargoMovement
from webapp.db.cargo_movement.models import AttachmentCargoMovement


def get_movements():
    return CargoMovement.query.filter().all()


def get_movement_by_id(id: int):
    return CargoMovement.query.filter(CargoMovement.id == id).first()


def get_attachments(movement_id: int):
    return AttachmentCargoMovement.query.filter(AttachmentCargoMovement.movement_id == movement_id).all()


def get_attachment_by_id(id: int):
    return AttachmentCargoMovement.query.filter(AttachmentCargoMovement.id == id).first()
