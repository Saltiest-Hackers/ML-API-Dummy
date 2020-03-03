import json
from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
CORS(app)
@app.route("/topcomments" )
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

    out = [{"c_id":21816249,"comment_text":"No, work stealing is pretty high overhead.","p_id":21815770,"saltiness":0.45,"timestamp":1576604821,"u_id":"zzzcpan"},{"c_id":22298216,"comment_text":"That&#x27;s the problem with Mozilla&#x27;s privacy propaganda, their funding depends on violating privacy, so they can only talk and pretend, but not actually do anything about it. Which makes them look bad, dishonest and fake, when they are talking about privacy.","p_id":22298151,"saltiness":0.379,"timestamp":1581427163,"u_id":"zzzcpan"},{"c_id":22146979,"comment_text":"Automated service for issuing DDoS attacks.","p_id":22146961,"saltiness":0.367,"timestamp":1579969967,"u_id":"zzzcpan"},{"c_id":21915908,"comment_text":"No, you should ignore OSI crap. They interpret &quot;open&quot; as open to be closed and abused by corporations, not remaining open for end users.","p_id":21915680,"saltiness":0.346,"timestamp":1577733730,"u_id":"zzzcpan"},{"c_id":22393042,"comment_text":"FAANG won&#x27;t stop, as they put people through hell on purpose. They want them to dread interviewing and switching jobs, so they can have them for themselves for longer and pay them less.","p_id":22387906,"saltiness":0.277,"timestamp":1582402189,"u_id":"zzzcpan"},{"c_id":22413614,"comment_text":"DoH can be blocked by IP addresses, DNS canary and probably SNI, while DoT by IP addresses and port number. So &quot;DoT is DoH with a kill switch.&quot; is again nonsense.","p_id":22413147,"saltiness":0.258,"timestamp":1582642322,"u_id":"zzzcpan"},{"c_id":22317374,"comment_text":"The problem doesn&#x27;t have a &quot;full solution&quot;, like any fault tolerance in general, only probabilistic one.","p_id":22317254,"saltiness":0.256,"timestamp":1581599013,"u_id":"zzzcpan"},{"c_id":21913363,"comment_text":"It&#x27;s just bad irrelevant title and blogspam level of content attempting to &quot;explain&quot; why big corporations suck at producing quality software.","p_id":21913340,"saltiness":0.252,"timestamp":1577714588,"u_id":"zzzcpan"},{"c_id":22044408,"comment_text":"Random UA can get you outright blocked for looking like a bot. So is faking Googlebot and such.","p_id":22044350,"saltiness":0.239,"timestamp":1579007385,"u_id":"zzzcpan"},{"c_id":22107785,"comment_text":"It&#x27;s the opposite of Moxie&#x27;s propaganda. Here&#x27;s an example of this conflict at play: <a href=\"https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=22106536\" rel=\"nofollow\">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=22106536</a>","p_id":22105636,"saltiness":0.233,"timestamp":1579620858,"u_id":"zzzcpan"},{"c_id":21913627,"comment_text":"On linux there is the best of both worlds approach. You can use zram for swap and userspace OOM killer, like earlyoom. If processes start using a bit more memory or leaking they won&#x27;t get killed and nothing will slow down much, but will get killed if things start to go too far to cause performance problems.","p_id":21913557,"saltiness":0.219,"timestamp":1577717329,"u_id":"zzzcpan"}]
    
    return app.response_class(
        response=json.dumps(out),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(port=9000, debug=True)