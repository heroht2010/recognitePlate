import pymysql as MySQLdb
import  config

def connection():
    try:
        db = MySQLdb.connect(host=config.mysql_host,
                             user=config.mysql_user,
                             passwd=config.mysql_pass,
                             db=config.mysql_db)
        return db
    except:
        print ("Can not connect to database")
        return None