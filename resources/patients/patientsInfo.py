from ..sqlConnection import getConnection
from flask_restful import Resource

class getPatientInfo(Resource):
    def get(self,doctor_number):
        cnx, mycurser = getConnection()
        command = 'SELECT _name, account_number from accounts WHERE supervised = %s;'%doctor_number
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 400
    
