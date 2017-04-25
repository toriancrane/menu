import os
import re
import webapp2
import jinja2
import hashlib
import hmac
import string
import random
import time
import db_methods

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                            autoescape = True)

def render_str(template, **params):
    """ Global render_str function """
    t = jinja_env.get_template(template)
    return t.render(params)

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
        res_list = db_methods.getAllRestaurants()
        self.render('restaurants.html', restaurants = res_list)

##############   New Restaurant Page    #############

class NewRestaurantPage(MasterHandler):
    """ Front Page Handler """
    def get(self):
        self.render('newrestaurant.html')

    def post(self):
        res_name = self.request.get('res_name')
        if res_name:
            db_methods.addNewRestaurant(res_name)
            time.sleep(0.1)
            self.redirect("/restaurants")
        else:
            error = "You need to enter the name of the restaurant you want to add."
            self.render('newrestaurant.html', error = error)

##############   New Restaurant Page    #############

class EditRestaurantPage(MasterHandler):
    """ Front Page Handler """
    def get(self):
        # Obtain specific restaurant id

        # Obtain text for name of restaurant
        #res_name = 

        # Render edit page with current restaurant name
        self.render('editrestaurant.html', res_name = res_name)

    def post(self):
        res_name = self.request.get('res_name')
        if res_name:
            # Obtain specific restaurant id

            # Modify the name of the restaurant
            db_methods.editRestaurant(res_name)
            time.sleep(0.1)
            self.redirect("/restaurants")
        else:
            error = "You need to enter the updated name of the restaurant."
            self.render('newrestaurant.html', error = error)     


##############    webapp2 Routes    #############

app = webapp2.WSGIApplication([
    ("/", FrontPage),
    ("/restaurants", RestaurantsPage),
    ("/restaurants/new", NewRestaurantPage),
    ("/restaurants/([0-9]+)/edit", EditRestaurantPage)
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()