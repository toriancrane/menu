import os
import re
import webapp2
import jinja2
import hashlib
import hmac
import string
import random
import time
import db_queries

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                            autoescape = True)

def render_str(template, **params):
    """ Global render_str function """
    t = jinja_env.get_template(template)
    return t.render(params)

def remove_unicode(list):
    l_temp = []
    for l in list:
        l_temp.append(l.encode('ascii'))
    return l_temp

class MasterHandler(webapp2.RequestHandler):
    """ MasterHandler Class """

#Jinja Methods
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

##############    Front Page    #############

class FrontPage(MasterHandler):
    """ Front Page Handler """
    def get(self):
        self.render('front.html')

##############   Restaurants Page    #############

class RestaurantsPage(MasterHandler):
    """ Front Page Handler """
    def get(self):
        res_list = db_queries.getAllRestaurants()
        res_list = remove_unicode(res_list)
        self.render('restaurants.html', restaurants = res_list)


##############    webapp2 Routes    #############

app = webapp2.WSGIApplication([
    ("/", FrontPage),
    ("/restaurants", RestaurantsPage)
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()