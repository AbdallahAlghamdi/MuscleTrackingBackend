from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

#---
class login(Resource):
    def get(self, username, password):
        cnx, mycursor = getConnection()
        command = "call login('%s', '%s')"%(username, password);
        mycursor.execute(command)
        result = mycursor.fetchall()
        if(mycursor.rowcount>0):
            return result, 200
        else:   
            return {'Status': 'Error'},404
