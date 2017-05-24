from .views import new_paste


def add_api_routes(app):
    app.add_route(new_paste, '/post/', methods=['POST'])
    # app.add_route(handler2, '/folder/<name>')
    # app.add_route(person_handler2, '/person/<name:[A-z]>', methods=['GET'])
