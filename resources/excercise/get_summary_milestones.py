from ..sqlConnection import getConnection
from flask_restful import Resource

class getSummaryMilestones(Resource):
    def get(self,account_number):
        cnx, mycurser = getConnection()
        command = "CALL get_summary_milestone(%d);"%account_number
        mycurser.execute(command)
        result = mycurser.fetchall()
        if(mycurser.rowcount >0):
            return result, 200
        return {'Status': 'Empty'}, 400