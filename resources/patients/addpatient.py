from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

class addPatient(Resource):
    def post(self,doctor_number, patient_number):
        cnx, mycurser = getConnection()
        cnx.autocommit = True
        command = "UPDATE accounts SET supervised = %d where account_number = %d AND _status = 'patient' AND supervised IS NULL"%(doctor_number, patient_number)
        print(command)
        mycurser.execute(command)
        print(mycurser.rowcount)
        if mycurser.rowcount> 0:
            return {'Status': 'Changed!'}, 200
        else: 
            return {'Status': "Error, can't add this as patient"}, 400
