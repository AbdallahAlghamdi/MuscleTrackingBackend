from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection
# def setAllAsRead(account_number):
#     cnx, mycurser = getConnection()
#     cnx.autocommit = True
#     command = 'UPDATE notifications set hasRead = 1 where recipient_id = %d;'%account_number
#     mycurser.execute(command)
   
class getMail(Resource):
    def get(self, account_number):
        
        cnx, mycurser = getConnection()
        command = 'CALL get_mail(%d);'%account_number
        print(command)
        mycurser.execute(command)
        result = mycurser.fetchall()
        # setAllAsRead(account_number)
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 401