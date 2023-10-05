import configparser
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Leia o arquivo de configuração INI
config = configparser.ConfigParser()
config_path = os.path.join(script_dir, 'config.ini')
config.read(config_path)
