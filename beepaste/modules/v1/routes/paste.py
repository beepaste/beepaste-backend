from beepaste.modules.v1.views.paste import PasteView


def init_paste_routes(app):
    app.add_route(PasteView.as_view(), '/')
    app.add_route(PasteView.as_view(), '/<pasteid>')
