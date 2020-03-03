import json
from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
CORS(app)
@app.route("/topcomments", methods=['POST'])
def topcomments():
    '''Dummy Response'''


    # use a dictionary to format output for json
    out = {"author": "iron0013", "comment_text": "Dupe.", "id": 22050083,
            "parent_id": 22049882, "saltiness": 1, "time": 1579042345}

    # give output to sender
    return app.response_class(
        response=json.dumps(out),
        status=200,
        mimetype='application/json'
    )

@app.route('/user/johndoe')
def username():

    out = {
    "c_id":21816249,"comment_text":"No, work stealing is pretty high overhead.",
    "p_id":21815770,"saltiness":0.45,"timestamp":1576604821,"u_id":"zzzcpan"},
    {"c_id":22298216,"comment_text":"That&#x27;s the problem with Mozilla&#x27;s\
        privacy propaganda, their funding depends on violating privacy, so they\
        can only talk and pretend, but not actually do anything about it.\
        Which makes them look bad, dishonest and fake, when they are\
        talking about privacy.","p_id":22298151,
        "saltiness":0.379,"timestamp":1581427163,"u_id":"zzzcpan"}
    
    return app.response_class(
        response=json.dumps(out),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(port=9000, debug=True)