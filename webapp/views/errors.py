from flask import render_template


ERROS_TEMPLATE = "crud_error.html"

def get_tempale_error_on_create_or_update(errors):
    return render_template(ERROS_TEMPLATE, content=f"error on create or update info {errors}")


def get_tempale_error_on_validation(errors):
    render_template(ERROS_TEMPLATE, content=f"error on validation {errors}")


def get_tempale_error_on_mark_for_deleting(errors):
    render_template(ERROS_TEMPLATE, content=f"error on mark for deleting {errors}")
