from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

#----Args---
excerciseData = reqparse.RequestParser()
excerciseData.add_argument("account_number", type = int, required=True, help="Account number must be present")
excerciseData.add_argument("average_data", type = float, required=True, help="Average data must be present")
excerciseData.add_argument("muscle_group", type = str, required=True, help="Muscle group name must be present")
excerciseData.add_argument("duration", type = int, required=True)
excerciseData.add_argument("raw_data", type = int, action="append", location='json')

def addExcerciseData(dicts):
    cnx, mycursor = getConnection()
    cnx.autocommit = True
    account_number = dicts["account_number"]
    average_data = dicts["average_data"]
    muscle_group = dicts["muscle_group"]
    duration = dicts["duration"]
    mycursor.execute("call new_excercise(%d, %.2f, '%s', %d)" %(account_number, average_data, muscle_group, duration))
    new_ID = mycursor.fetchone()['LAST_INSERT_ID()']
    cnx.close()
    mycursor.close()
    addRawData(new_ID, dicts["raw_data"])

def addRawData(id ,dicts):
    for i in dicts:
        cnx, mycursor = getConnection()
        cnx.autocommit = True
        mycursor.execute("INSERT INTO raw_data(value, excercise_id) values (%d, %d)"%(i, id))
#----
class addExcercise(Resource):
    def post(self):
        args = excerciseData.parse_args()
        print(args)
        addExcerciseData(args)
        return {'status':'added'}
    
