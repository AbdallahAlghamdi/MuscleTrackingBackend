from flask import Flask
from flask_restful import Api
from resources.Login.signup import newAccount
from resources.excercise.get_patient_milestones import getPatientMilestones
from resources.excercise.get_summary_milestones import getSummaryMilestones
from resources.mail.getMail import getMail
from resources.getRecipients import getRecipients
from resources.mail.getNotifications import getNotifiactions
from resources.mail.getSentMail import getSentMail
from resources.mail.newMail import addMailMessage
from resources.mail.setMailReady import setMailReady
from resources.patients.addpatient import addPatient
from resources.patients.patientsInfo import getPatientInfo
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
api.add_resource(login,'/login/<username>/<password>')
api.add_resource(addExcercise, '/newExcercise')
api.add_resource(getAvgExcercise, '/getavg/<int:account_number>/<muscle_group>/<duration>')
api.add_resource(getExcerciseID, '/getExcerciseID/<int:account_number>/<muscle_group>/<duration>')
api.add_resource(getDetailExercise, '/getDetailExercise/<int:exercise_id>')
api.add_resource(getPatientInfo,'/getPatientInfo/<int:doctor_number>')
api.add_resource(addPatient,'/addPatient/<int:doctor_number>/<int:patient_number>')
api.add_resource(getRecipients, '/getRecipients/<int:account_number>')
api.add_resource(getMail, '/getMail/<int:account_number>')
api.add_resource(addMailMessage, '/newMail')
api.add_resource(getSentMail, '/getSentMail/<int:account_number>')
api.add_resource(newAccount, '/signUp')
api.add_resource(setMailReady, '/readMail/<int:messageID>')
api.add_resource(getNotifiactions, '/getNotifications/<int:account_number>')
api.add_resource(getSummaryMilestones, '/getSummary/<int:account_number>')
api.add_resource(getPatientMilestones, '/getPatientSummary/<int:account_number>/<duration>')


if __name__ == '__main__':
    app.run( debug=True)
    # http_server = WSGIServer(('', 8080), app)
    # http_server.serve_forever()

    