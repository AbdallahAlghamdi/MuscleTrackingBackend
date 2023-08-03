from resources.sqlConnection import getConnection
from flask_restful import Resource, Api, reqparse


class VideoCheck(Resource):
    def get(self, video_id):
        mycursor = getConnection()
        mycursor.execute('select * from videos where ID=', video_id )
        result = mycursor.fetchall()
        
        return result,222
        
        