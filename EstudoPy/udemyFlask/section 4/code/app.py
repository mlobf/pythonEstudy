from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)


items = []


class Item(Resource):
    def get(self, name):
        # Send the Correct Item to broswer, no more need to use jsonify --Flask-RESTful does it
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):  # Create Item under REST perspective
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": "An item with name {} already exists.".format(name)}, 400

        data = request.get_json(force=True)
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}


#    def post(self):

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")


app.run(port=5000, debug=True)
