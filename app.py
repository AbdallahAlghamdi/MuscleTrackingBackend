from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.video.videoSubmission import VideoSubmission
from resources.video.videoCheck import VideoCheck
from gevent.pywsgi import WSGIServer

#-----
app = Flask(__name__)
api = Api(app)


api.add_resource(VideoSubmission, "/videoSubmission")
api.add_resource(VideoCheck, "/video/<int:video_id>")
    

if __name__ == '__main__':
    
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()

    