from gevent import monkey
monkey.patch_all()
import falcon
from app.sso import checkMyauth
import ujson as json
with open('.hash.conf','r') as fp:
  passwd=json.load(fp)['pass']
keys=set(['id_tag','secret','timestamp'])
# checkMyauth(id_tag: str, secret: str, clienttime: str, passwd: str) -> bool
class sudaauth(object):
  def on_get(self, req, resp):
    if keys & req.params.keys():
      print(req.params)
      id_tag=req.params['id_tag']
      secret=req.params['secret']
      timestamp=req.params['timestamp']
      name=req.params['name']
      usertype=req.params['usertype']
      print("id_tag:{}\nsecret:{}\ntimestamp:{}".format(id_tag,secret,timestamp))
      res=checkMyauth(id_tag=id_tag,secret=secret,clienttime=timestamp,passwd=passwd)
      print()
      resp.status = falcon.HTTP_200
      if res:
        resp.body=json.dumps({"status":"ok","data":{"id":id_tag,"name":name,"usertype":usertype}})
      else:
        resp.bosy=json.dumps({"status":"error","data":"Timed Out"})
    else:
      resp.status = falcon.HTTP_404
      resp.body='Logouted\n'

class logout(object):
  def on_get(self,req,resp):
    resp.status = falcon.HTTP_200
    resp.body='Logouted\n'
    
api = application = falcon.API()

auth=sudaauth()
logouter=logout()
api.add_route('/login', auth)
api.add_route('/logout',logouter)
