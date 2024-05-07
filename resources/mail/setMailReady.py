from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

class setMailReady(Resource):
    def put(self, messageID):
        cnx, mycurser = getConnection()
        cnx.autocommit = True
        command = 'UPDATE notifications set hasRead = 1 where message_id = %d;'%messageID
        mycurser.execute(command)
        return {'Status': 'Read!'}, 200