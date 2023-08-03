from flask_restful import Resource, Api, reqparse
from resources.sqlConnection import getConnection
import mysql.connector

#----Args---
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("Name", type = str, help="Error, expecting String for name of video")
video_put_args.add_argument("Views", type = int, help="Error, expecting Int for Views of video")
video_put_args.add_argument("Likes", type = int, help="Error, expecting Int for Likes of video")

#----
def addMovie(dictS):
    cnx, mycursor = getConnection()
    name = dictS['Name']
    print("NAME: ", name)
    views = dictS['Views']
    print('Views: ', views)
    likes = dictS['Likes']
    print('likes: ', likes)
    print("END RESULT: insert into videos(Name, Views, Likes) values('%s', %d, %d)" % (name, views, likes))
    mycursor.execute("insert into videos(Name, Views, Likes) values('%s', %d, %d)" % (name, views, likes))
    cnx.commit()
    mycursor.close()
    cnx.close()

class VideoSubmission(Resource):
    def put(self):
        args = video_put_args.parse_args()
        addMovie(args)
        return  201