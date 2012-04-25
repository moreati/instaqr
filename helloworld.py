import os

import jinja2

import webapp2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self, url):
        width = 300
        height = 300
        values = {
            'url': url,
            'img_url': '//chart.apis.google.com'
                       '/chart?cht=qr&chs=%ix%i&chld=H|0&chl=%s'
                       % (width, height, url),
            'width': width,
            'height': height,
            }
        template = jinja_env.get_template('index.html')
        self.response.out.write(template.render(values))


app = webapp2.WSGIApplication([
        ('/(.+)', MainPage),
        ],
        debug=True)
