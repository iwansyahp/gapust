__author__ = 'Iwansyah Putra'

import os
import jinja2
import webapp2
import service_account

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# Class yang digunakan untuk memuat halaman index kosong
#
class IndexPage(webapp2.RequestHandler):
  """ The API Checker dashboard home page. """
  def get(self):
    temp_val = {}
    template = jinja_env.get_template('templates/index.html')
    self.response.out.write(template.render(temp_val))

# Arahkan index langsung ke halaman statistik
class OpacAnalyticPage(webapp2.RequestHandler):
  """ Halaman data analytics yang terkumpul (menggunakan server side auth). """
  def get(self):
    
    access_token = service_account.get_access_token()
    temp_val = {'access_token': access_token, 'situs': 'OPAC'}    
    template = jinja_env.get_template('templates/opacserveanalytics.html')
    self.response.out.write(template.render(temp_val))

class EtdAnalyticPage(webapp2.RequestHandler):
  """ Halaman data analytics yang terkumpul (menggunakan server side auth). """
  def get(self):
    
    access_token = service_account.get_access_token()
    temp_val = {'access_token': access_token, 'situs': 'ETD'}    
    template = jinja_env.get_template('templates/etdserveanalytics.html')
    self.response.out.write(template.render(temp_val))

class OpenAccessAnalyticPage(webapp2.RequestHandler):
  """ Halaman data analytics yang terkumpul (menggunakan server side auth). """
  def get(self):
    
    access_token = service_account.get_access_token()
    temp_val = {'access_token': access_token, 'situs': 'Open Access Unsyiah'}    
    template = jinja_env.get_template('templates/openaccessserveanalytics.html')
    self.response.out.write(template.render(temp_val))

class UilisAnalyticPage(webapp2.RequestHandler):
  """ Halaman data analytics yang terkumpul (menggunakan server side auth). """
  def get(self):
    
    access_token = service_account.get_access_token()
    temp_val = {'access_token': access_token, 'situs': 'UILIS'}    
    template = jinja_env.get_template('templates/uilisserveanalytics.html')
    self.response.out.write(template.render(temp_val))

class OpacRedirectPage(webapp2.RequestHandler):
  def get(self):
    self.redirect("http://uilis.unsyiah.ac.id/opac")
class EtdRedirectPage(webapp2.RequestHandler):
  def get(self):
    self.redirect("http://uilis.unsyiah.ac.id/etd")
class OpenAccessRedirectPage(webapp2.RequestHandler):
  def get(self):
    self.redirect("http://openaccess.unsyiah.ac.id")
class UilisRedirectPage(webapp2.RequestHandler):
  def get(self):
    self.redirect("http://uilis.unsyiah.ac.id")

app = webapp2.WSGIApplication([
  ('/', IndexPage),
  ('/opac', OpacAnalyticPage),
  ('/etd', EtdAnalyticPage),
  ('/openaccess', OpenAccessAnalyticPage),
  ('/uilis', UilisAnalyticPage),
  ('/opac.unsyiah.ac.id', OpacRedirectPage),
  ('/etd.unsyiah.ac.id', EtdRedirectPage),
  ('/openaccess.unsyiah.ac.id', OpenAccessRedirectPage),
  ('/uilis.unsyiah.ac.id', UilisRedirectPage),
  ])
