import configparser
import yaml

config = configparser.ConfigParser()
config.read("ini.ini", encoding="utf-8")

data = {}
for section in config.sections():
    data[section] = dict(config[section])

with open("file.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

