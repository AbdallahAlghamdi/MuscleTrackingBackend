from ..sqlConnection import getConnection
from flask_restful import Resource

class getAvgExcercise(Resource):
    def get(self,account_number, muscle_group, duration):
        cnx, mycurser = getConnection()
        # command = "SELECT average_data from exercise_data where muscle_group = '%s' and account_number = %d LIMIT 7"%(muscle_group,account_number)
        command = "CALL get_Avg_Exercise(%d,'%s',%s);"%(account_number, muscle_group, duration)
        print(command)
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 401
    
class getDetailExercise(Resource):
    def get(self,exercise_id):
        cnx, mycurser = getConnection()
        command = "SELECT value from raw_data where excercise_id = '%s'"%(exercise_id)
        print(command)
        mycurser.execute(command)
        result = mycurser.fetchall()
        print(result)
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 401
class getExcerciseID(Resource):
    def get(self, account_number, muscle_group,duration):
        cnx, mycurser = getConnection()
        # command = "SELECT average_data from exercise_data where muscle_group = '%s' and account_number = %d LIMIT 7"%(muscle_group,account_number)
        command = "CALL get_Exercise_IDs(%d,'%s',%s);"%(account_number, muscle_group, duration)
        print(command)
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 401
    
