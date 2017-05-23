import os


def get_config(section):
    dirname = os.path.dirname
    try:
        conf_file = dirname(os.path.realpath(__file__)) + '/confi2g.yaml'
        with open(conf_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
    except FileNotFoundError:
        #TODO: Log this
        return {}
    try:
        return cfg[section]
    except KeyError:
        #TODO: Log this
        return {}
