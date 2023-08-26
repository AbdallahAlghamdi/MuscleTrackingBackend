from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection

#----Args---
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("username", type = str, help="Error, expecting String for username")
video_put_args.add_argument("password", type = str, help="Error, expecting String for password")

#---
class login(Resource):
    def post(self):
        args = video_put_args.parse_args()
        cnx, mycursor = getConnection()
        print('%s and %s'%(args["username"], args["password"]))
        command = 'select _status from Accounts where username = \'%s\' and _password = \'%s\' '%(args['username'], args['password'] )

        mycursor.execute(command)
        
        result = mycursor.fetchall()
        if(mycursor.rowcount>0):
            print(list(mycursor))
            return result, 999
        else:   
            return {"ERROR_ID":"NO RESULT"}
