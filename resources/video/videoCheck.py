from resources.sqlConnection import getConnection
from flask_restful import Resource, Api, reqparse




class VideoCheck(Resource):
    def get(self, video_id):
        cnx, mycursor = getConnection()
        count = mycursor.execute('select * from videos where ID = ' + str(video_id) )
       
        result = mycursor.fetchall()
    
        if(mycursor.rowcount>0):
            return result, 999
        else:
            return {"ERROR_ID":"NO RESULT"}
        
        
        
        
        