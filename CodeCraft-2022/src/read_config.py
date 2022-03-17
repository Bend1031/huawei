import configparser

config = configparser.ConfigParser()
config.read("data\config.ini")

Q = config.getint('config', 'qos_constraint')
