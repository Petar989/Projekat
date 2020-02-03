#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        #return self.response.write('Hello Weather!')
        return self.render_template("index.html")


class CalcHandler(BaseHandler):
    def get(self):
        return self.render_template("calc1.html")


class GuestbookHandler(BaseHandler):
    def get(self):
        return self.render_template("guest.html")

class ConverterHandler(BaseHandler):
    def get(self):
        return self.render_template("konvertsjavu.html")

class WeatherHandler(webapp2.RequestHandler):
        def get(self):
            return self.response.write('Hello Weather!')


class CVHandler (webapp2.RequestHandler):
        def get(self):
            return self.response.write('Hello CV!')

class SecretNumHandler(webapp2.RequestHandler):
        def get(self):
            return self.response.write('Hello SecretNum!')


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello Login!')

class MsglistHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello Msg list!')

class NekihtmlHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('<strong>Neki naslov</strong>' )

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/calc', CalcHandler),
    webapp2.Route('/guestbook', GuestbookHandler),
    webapp2.Route('/converter', ConverterHandler),
    webapp2.Route('/weather', WeatherHandler),
    webapp2.Route('/cv', CVHandler),
    webapp2.Route('/secretnum', SecretNumHandler),
    webapp2.Route('/login', LoginHandler),
    webapp2.Route('/msg', MsglistHandler),
    webapp2.Route('/nekihtml', NekihtmlHandler),
], debug=True)
