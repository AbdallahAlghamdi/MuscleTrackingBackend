from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection
class getSentMail(Resource):
    def get(self, account_number):
        cnx, mycurser = getConnection()
        command = 'CALL get_sent_mail(%d);'%account_number
        print(command)
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 401