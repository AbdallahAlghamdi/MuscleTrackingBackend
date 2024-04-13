from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

class getMail(Resource):
    def get(self, account_number):
        cnx, mycurser = getConnection()
        command = 'CALL get_mail(%d);'%account_number
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 400