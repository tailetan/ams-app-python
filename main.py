import webapp2
from handlers.AssetHandler import AssetHandler
from handlers.UserHandler import *
from handlers.CategoryHandler import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')

routes = [
    (r'/user', UserHandler),
    (r'/user/', UserHandler),
    (r'/user/<user_id:[a-zA-Z0-9]*>', UserHandler),
    (r'/category', CategoryHandler),
    (r'/asset', AssetHandler)

]
application = webapp2.WSGIApplication(routes=routes, debug=True)

def main():
    application.RUN()


if __name__ == '__main__':
    main()
