from .views import DocView


def init_doc_routes(app):
    app.add_route(DocView.as_view(), '/')
