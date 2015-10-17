__author__ = 'Ritesh_Ranjan'
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('../templates/config.properties')

dbname =  config.get('DatabaseSection', 'database.dbname')
dbpassword =  config.get('DatabaseSection', 'database.password')
dbuser =  config.get('DatabaseSection', 'database.user')
dbtype = config.get('DatabaseSection', 'database.type')
dbschema = config.get('DatabaseSection', 'database.schema')
