from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection
cnx, mycurser = getConnection()
cnx.autocommit = True
def updateRow(patientID, duration, muscleGroup, durationGroup):
    command = "UPDATE milestones SET %s = %d WHERE patient_id = %d AND muscleGroup = '%s';"%(durationGroup, duration, patientID, muscleGroup)
    print(command)
    mycurser.execute(command)
    mycurser.fetchall()
    return mycurser.rowcount > 0
def insertNewRow(patientID, duration, muscleGroup, durationGroup):
    command = "INSERT INTO milestones(patient_id, muscleGroup) values (%d, '%s')"%(patientID, muscleGroup)
    print(command)

    mycurser.execute(command)
    updateRow(patientID, duration, muscleGroup, durationGroup)
class newMilestone(Resource):
    def post(self,patientID, duration, muscleGroup, durationGroup):
        if(updateRow(patientID, duration, muscleGroup, durationGroup)):
            return {'Status':'updated'}, 200
        else:
            insertNewRow(patientID, duration, muscleGroup, durationGroup)   
            return {'Status': 'Inserted'}, 200
    
    