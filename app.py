from flask import Flask
from flask_restful import Api
from resources.video.videoSubmission import VideoSubmission
from resources.video.videoCheck import VideoCheck
from resources.video.VideoID import GetVideoIDs
from resources.Login.login import login
from resources.excercise.new_excercise import addExcercise
from resources.excercise.excercise import getAvgExcercise, getExcerciseID, getDetailExercise
from gevent.pywsgi import WSGIServer


#-----
app = Flask(__name__)
api = Api(app)


api.add_resource(VideoSubmission, "/videoSubmission")
api.add_resource(VideoCheck, "/video/<int:video_id>")
api.add_resource(GetVideoIDs, "/videosList")
api.add_resource(login,'/login')
api.add_resource(addExcercise, '/newExcercise')
api.add_resource(getAvgExcercise, '/getavg/<int:account_number>/<muscle_group>')
api.add_resource(getExcerciseID, '/getExcerciseID/<int:account_number>/<muscle_group>')
api.add_resource(getDetailExercise, '/getDetailExercise/<int:exercise_id>')



if __name__ == '__main__':
    # app.run( debug=True)
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()

    