from webapp.app import create_app
from webapp.db.utils.route_utils import point_list_update
from webapp.db.utils.route_utils import routes_update


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # point_list_update()
        routes_update()
