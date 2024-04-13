from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

#----Args---
messageData = reqparse.RequestParser()
messageData.add_argument("sender", type = int, required=True, help="Sender account number must be present")
messageData.add_argument("receiver", type = int, required=True, help="Receiver account number must be present")
messageData.add_argument("message_content", type = str, required=True, help="Mail content must not be empty or null")
messageData.add_argument("message_title", type = str, required=True, help="Mail title must not be empty or null")

def addMailToDatabase(dicts):
        cnx, mycursor = getConnection()
        cnx.autocommit = True
        sender = dicts["sender"]
        receiver = dicts["receiver"]
        message_content = dicts["message_content"]
        message_title = dicts["message_title"]
        command = "call new_mail(%d,%d,'%s', '%s');"%(sender, receiver, message_content,message_title)
        mycursor.execute(command)
        cnx.close()
        mycursor.close()
class addMailMessage(Resource):
    def post(self):
        args = messageData.parse_args()
        addMailToDatabase(args)
        return {'status':'added'}
