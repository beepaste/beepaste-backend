from .views import get_paste, post_paste, new_api_token


def add_api_routes(app):
    app.add_route(get_paste, '/paste', methods=['GET'])
    app.add_route(post_paste, '/paste', methods=['POST'])
    app.add_route(new_api_token, '/authorize', methods=['GET'])
    # app.add_route(handler2, '/folder/<name>')
    # app.add_route(person_handler2, '/person/<name:[A-z]>', methods=['GET'])
