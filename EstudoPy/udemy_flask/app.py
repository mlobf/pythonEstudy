from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderfull Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# POST / store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    return ""

# GET / store/<string:name>


@app.route("/store/<string:name>")
def get_store(name):
    return ""


# GET /store
@app.route("/store/")
def get_stores():
    return ""

# POST / store/<string:name>item {name:, price:}


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store():
    return ""

# GET /store/<string:name>/item


@app.route("/store/<string:name>/item")
def get_item_in_store():
    return ""


app.run(port=5000)