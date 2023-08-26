from flask_restful import Resource
from resources.sqlConnection import getConnection
class GetVideoIDs(Resource):
    def get(self):
        cnx, mycursor = getConnection()
        
        command = 'select ID from videos'
        mycursor.execute(command)
        
        result = mycursor.fetchall()
        if(mycursor.rowcount>0):
            print(list(mycursor))
            return result, 999
        else:   
            return {"ERROR_ID":"NO RESULT"}