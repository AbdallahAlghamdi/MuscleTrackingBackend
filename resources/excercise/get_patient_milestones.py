from ..sqlConnection import getConnection
from flask_restful import Resource

class getPatientMilestones(Resource):
    def get(self,account_number, duration):
        cnx, mycurser = getConnection()
        command = "CALL getPatientMilestones(%d,'%s');"%(account_number,duration )
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 400