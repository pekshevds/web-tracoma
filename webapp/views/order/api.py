from flask import render_template, redirect, url_for, current_app as app
from webapp.db.storage.fetchers import get_carriers, get_counteragents
from webapp.db.point.fetchers import get_points
from webapp.db.order.fetchers import get_orders, get_attachments, get_attachment_by_id
from webapp.db.order.changers import delete_order, delete_attachment
from webapp.db.order.models import Attachment, db
from webapp.views.order.forms import OrderForm, AttachmentForm
from webapp.views.common import BaseView
from flask_views.base import TemplateView

from sqlalchemy import func

from webapp.db.utils.route_utils import fetch_distance_between_cities


class OrderDetailView(BaseView):
    form_class = OrderForm
    template_name = 'order_item.html'
    self_url_name = 'order.show_order'

    def get(self, *args, **kwargs):
        order_id = kwargs.get("id", 0)
        object = super().get_object_by_id(id=order_id)
        if object:
            form = super().initial_form_values(object)
        else:
            form = self.get_form()
        return render_template(self.template_name, form=form,
                               carriers=get_carriers(),
                               counteragents=get_counteragents(),
                               points=get_points(),
                               attachments=get_attachments(order_id=order_id))

    def __calculate_order_weight_and_volume(self, object: object) -> dict:
        weight_and_volume = db.session.query(func.sum(Attachment.weight).label('total_weight'),
                                             func.sum(Attachment.volume).label('total_weight')).filter(
            Attachment.order_id == object.id
        ).first() or (0, 0)
        return {
            'weight': weight_and_volume[0],
            'volume': weight_and_volume[1]
        }

    def pre_save(self, object: object) -> None:
        object.distance = fetch_distance_between_cities(point_a=object.point_from.location,
                                                        point_b=object.point_to.location)
        weight_and_volume = self.__calculate_order_weight_and_volume(object)

        cost_per_weight = weight_and_volume.get('weight', 0) * app.config['COST_KG_PER_KM'] * object.distance
        cost_per_volume = weight_and_volume.get('volume', 0) * app.config['COST_M3_PER_KM'] * object.distance
        object.cost = max(cost_per_weight, cost_per_volume)


class OrderListView(TemplateView):
    template_name = 'order_list.html'

    def get(self, *args, **kwargs):
        return render_template(self.template_name, orders=get_orders())


class OrderDeleteView(TemplateView):
    success_url_name = 'order.orders'

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        if delete_order(id=id):
            return redirect(url_for('order.orders'))
        return render_template("crud_error.html", content='error on mark point for deleting')


class AttachmentOrderDetailView(BaseView):
    form_class = AttachmentForm
    template_name = 'order_attachment_item.html'
    self_url_name = 'order.show_attachment'

    def get(self, *args, **kwargs):
        object = self.get_object_by_id(id=kwargs.get("id", 0))
        if object:
            form = self.initial_form_values(object)
        else:
            form = self.get_form()
            form.order_id.data = kwargs.get("order_id", 0)
        return render_template(self.template_name, form=form)


class AttachmentOrderListView(TemplateView):
    template_name = 'order_attachment_list.html'

    def get(self, *args, **kwargs):
        order_id = kwargs.get("order_id", 0)
        return render_template(self.template_name, attachments=get_attachments(order_id=order_id))


class AttachmentOrderDeleteView(TemplateView):

    def get(self, *args, **kwargs):
        id = kwargs.get("id", 0)
        attachment = get_attachment_by_id(id=id)
        order_id = attachment.order_id
        if delete_attachment(id=id):
            return redirect(url_for('order.show_order', id=order_id))
        return render_template("crud_error.html", content='error on mark point for deleting')
