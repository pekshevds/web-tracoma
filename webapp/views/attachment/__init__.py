from flask import render_template, redirect, url_for
from webapp.db.attachment.fetchers import get_attachment_by_id, get_attachments
from webapp.db.attachment.changers import delete_attachment, save_attachment
from webapp.views.attachment.forms import AttachmentForm


def attachments_view(order_id: int):
    return render_template('attachment_list.html', attachments=get_attachments(order_id=order_id))


def attachment_view(attachment_id: int):
    attachment = get_attachment_by_id(id=attachment_id)
    form = AttachmentForm(obj=attachment)

    return render_template('attachment_item.html', form=form)


def new_attachment_view(order_id: int):
    form = AttachmentForm()
    form.order_id.data = order_id
    return render_template('attachment_item.html', form=form)


def save_attachment_view():
    form = AttachmentForm()
    print(form.data)
    if form.validate_on_submit():
        if save_attachment(form):
            return redirect(url_for('show_order', order_id=form.order_id.data))
        return render_template("crud_error.html", content='error on create or update storage info')
    return render_template("crud_error.html", content=f"error on validation {form.errors}")


def delete_attachment_view(attachment_id: int):
    if delete_attachment(id=attachment_id):
        attachment = get_attachment_by_id(id=attachment_id)
        return redirect(url_for('show_order', order_id=attachment.id))
    return render_template("crud_error.html", content='error on mark attachment for deleting')
