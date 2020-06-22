#This is simple app

from flask import Flask


app = Flask(__name__)

#Post  - receive data
#Get  - send data back only
@app.route('/store', methods=['POST'])
def create_store():
    pass
# GET/store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass
# GET/store
# POST/store/<string:name>/item{name:,price:}
# GET /store/<string:name>/item






app.run(port=5000)



