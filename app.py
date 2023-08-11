from flask import Flask
from flask_restful import Api
from resources.video.videoSubmission import VideoSubmission
from resources.video.videoCheck import VideoCheck
from resources.video.VideoID import GetVideoIDs
#from gevent.pywsgi import WSGIServer

#-----
app = Flask(__name__)
api = Api(app)


api.add_resource(VideoSubmission, "/videoSubmission")
api.add_resource(VideoCheck, "/video/<int:video_id>")
api.add_resource(GetVideoIDs, "/videosList")

if __name__ == '__main__':
    app.run(ssl_context="adhoc")
    app.run(debug=True)
    #http_server = WSGIServer(('', 8080), app)
    #http_server.serve_forever()

    