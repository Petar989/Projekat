#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello SmartNinja!')


class CalcHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello Cal!')


class GuestbookHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello Guestbook !')

class ConverterHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello Convereter!')

class WeatherHandler(webapp2.RequestHandler):
        def get(self):
            return self.response.write('Hello Weather!')


class CVHandler (webapp2.RequestHandler):
        def get(self):
            return self.response.write('Hello CV!')

class SecretNumHandler(webapp2.RequestHandler):
        def get(self):
            return self.response.write('Hello SecretNum!')

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/calc', CalcHandler),
    webapp2.Route('/guestbook', GuestbookHandler),
    webapp2.Route('/converter', ConverterHandler),
    webapp2.Route('/weather', WeatherHandler),
    webapp2.Route('/cv', CVHandler),
    webapp2.Route('/secretnum', SecretNumHandler),



], debug=True)

