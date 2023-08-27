from resources.sqlConnection import getConnection
from flask_restful import Resource, Api, reqparse




class GetVideoIDs(Resource):
    def get(self):
        cnx, mycursor = getConnection()
        count = mycursor.execute('select ID from videos' )
       
        result = mycursor.fetchall()
    
        if(mycursor.rowcount>0):
            
            return result, 999
        else:
            return {"ERROR_ID":"NO RESULT"}
        
        
        
        
        