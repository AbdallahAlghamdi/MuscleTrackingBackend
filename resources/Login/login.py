from flask_restful import Resource, reqparse
from resources.sqlConnection import getConnection


#---
class login(Resource):
    def get(self, username, password):
        cnx, mycursor = getConnection()
        command = "call login('%s', '%s')"%(username, password);
        print("\n\n"+ command +"\n\n")

        mycursor.execute(command)
        
        result = mycursor.fetchall()
        if(mycursor.rowcount>0):
            print("Entered row coutn")

            if result:
                print("list is not empty")
            else: print("list is empty")
            print(list(mycursor))
            return result, 200
        else:   
            return {'Status': 'Error'},404
