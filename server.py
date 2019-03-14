import falcon
from app.sso import checkMyauth
keys=set(['id_tag','secret','timestamp'])
passwd='test'
# checkMyauth(id_tag: str, secret: str, clienttime: str, passwd: str) -> bool
class sudaauth(object):
  def on_get(self, req, resp):
    if keys & req.params.keys():
      id_tag=req.params['id_tag']
      secret=req.params['secret']
      timestamp=req.params['timestamp']
      res=checkMyauth(id_tag=id_tag,secret=secret,clienttime=timestamp,passwd=passwd)
      resp.status = falcon.HTTP_200
      resp.body="Success "+str(res)
    else:
      resp.status = falcon.HTTP_404
      resp.body='Not Allowed'

    
api = application = falcon.API()

auth=sudaauth()
api.add_route('/', auth)