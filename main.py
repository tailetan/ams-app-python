import webapp2
from handlers.AssetHandler import AssetHandler
from handlers.UserHandler import *
from handlers.CategoryHandler import *

import sys

reload(sys)
sys.setdefaultencoding('utf8')

routes = [
    webapp2.Route(r'/api/user', UserHandler),
    webapp2.Route(r'/api/user/', UserHandler),
    webapp2.Route(r'/api/user/<user_id:[a-zA-Z0-9]*>', UserHandler),
    # webapp2.Route(r'/user/<user_id:[a-zA-Z0-9]*>', UserHandler, handler_method='get_entity_by_id'),

    (r'/api/category', CategoryHandler),
    (r'/api/asset', AssetHandler)

]
application = webapp2.WSGIApplication(routes=routes, debug=True)


def main():
    application.RUN()



if __name__ == '__main__':
    main()
    print "Content-Type: text/turtle"
    print "Content-Location: mydata.ttl"
    print "Access-Control-Allow-Origin: *"
    print
