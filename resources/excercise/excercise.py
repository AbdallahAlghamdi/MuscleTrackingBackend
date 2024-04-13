from ..sqlConnection import getConnection
from flask_restful import Resource

class getAvgExcercise(Resource):
    def get(self,account_number, muscle_group, duration):
        cnx, mycurser = getConnection()
        command = "CALL get_Avg_Exercise(%d,'%s',%s);"%(account_number, muscle_group, duration)
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 400
class getExcerciseID(Resource):
    def get(self, account_number, muscle_group,duration):
        cnx, mycurser = getConnection()
        command = "CALL get_Exercise_IDs(%d,'%s',%s);"%(account_number, muscle_group, duration)
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 400
class getDetailExercise(Resource):
    def get(self,exercise_id):
        cnx, mycurser = getConnection()
        command = "SELECT value from raw_data where excercise_id = '%s'"%(exercise_id)
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 400
    
