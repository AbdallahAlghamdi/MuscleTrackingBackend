import mysql.connector

def getConnection():
    cnx = mysql.connector.connect(
    username = "doadmin",
    password = "AVNS_-uTU9YDbmWAfDZ-MHuM",
    host = "balmung-do-user-14468201-0.b.db.ondigitalocean.com",
    port = "25060",
    database = "defaultdb" )
    return cnx ,cnx.cursor()