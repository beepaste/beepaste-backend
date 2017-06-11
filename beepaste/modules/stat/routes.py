from .views import StatView


def init_stat_routes(app):
    app.add_route(StatView.as_view(), '/')
