from ..sqlConnection import getConnection
from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

#----Args---
messageData = reqparse.RequestParser()
messageData.add_argument("username", type = str, required=True, help="Username must be present")
messageData.add_argument("password", type = str, required=True, help="Password must be present")
messageData.add_argument("accountType", type = str, required=True, help="AccountType must not be empty or null")
messageData.add_argument("accountName", type = str, required=True, help="AccountName must not be empty or null")

def newSignup(dicts):
        cnx, mycursor = getConnection()
        cnx.autocommit = True
        username = dicts["username"]
        password = dicts["password"]
        accountType = dicts["accountType"]
        accountName = dicts["accountName"]
        command = "call new_sign_up('%s','%s','%s', '%s');"%(accountType, accountName, username,password)
        print(command);
        mycursor.execute(command)
        cnx.close()
        mycursor.close()
class newAccount(Resource):
    def post(self):
        args = messageData.parse_args()
        print("-------------")
        print(args)
        print("-------------")
        newSignup(args)
        return {'status':'added'}
