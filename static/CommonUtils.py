__author__ = 'Ritesh_Ranjan'
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.properties')

dbname =  config.get('DatabaseSection', 'database.dbname');
dbpassword =  config.get('DatabaseSection', 'database.dbpassword');
dbuser =  config.get('DatabaseSection', 'database.dbuser');
dbtype = config.get('DatabaseSection', 'database.dbtype');