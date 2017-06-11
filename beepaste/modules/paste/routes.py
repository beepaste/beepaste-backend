from .views import PasteView


def init_paste_routes(app):
    app.add_route(PasteView.as_view(), '/')
