from beepaste.modules.v1.views.auth import AuthView


def init_auth_routes(app):
    app.add_route(AuthView.as_view(), '/auth')
    pass
