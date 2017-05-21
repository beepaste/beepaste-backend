import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

api_config = cfg['api']
