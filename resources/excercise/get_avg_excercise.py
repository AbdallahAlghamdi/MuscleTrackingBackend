from ..sqlConnection import getConnection
from flask_restful import Resource

class getAvgExcercise(Resource):
    def get(self,account_number, muscle_group):
        cnx, mycurser = getConnection()
        command = "SELECT average_data from exercise_data where muscle_group = '%s' and account_number = %d LIMIT 7"%(muscle_group,account_number)
        print(command)
        mycurser.execute(command)
        result = mycurser.fetchall()
        return result, 200
    