from flask import Flask from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Student(Resource):
    
    def get(self, name):
        return {"student": name}


#    def post(self):

api.add_resource(Student, "/student/<string:name>")

app.run(port=5000, debug=True)
