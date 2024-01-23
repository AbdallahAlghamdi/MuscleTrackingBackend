from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

class addPatient(Resource):
    def post(self,doctor_number, patient_number):
        cnx, mycurser = getConnection()
        cnx.autocommit = True
        command = 'UPDATE accounts set supervised = %d WHERE account_number = %d'%(doctor_number, patient_number)
        print(command)
        mycurser.execute(command)
        return {'Status': 'Changed!'}, 200
