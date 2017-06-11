from .views import AuthView


def init_auth_routes(app):
    app.add_route(AuthView.as_view(), '/')
    pass
