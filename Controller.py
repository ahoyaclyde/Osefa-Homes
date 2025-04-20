import asyncio
from flask import Flask , url_for , render_template , request , redirect , send_from_directory
from jinja2 import Environment , FileSystemLoader
from flask.views import View
from flask import g
import os , random , string 
import json 
from werkzeug.utils import secure_filename
import time
import sqlite3
from sqlite3 import Error
from flask_cors import CORS 
import uuid
import datetime
#from flask_sslify import SSLify

from utils import base as base 

#import Twilio_Content_Provider as Twilio_Service
app=Flask(__name__)
#sslify = SSLify(app)
app.config.update(
    PERMANENT_SESSION_LIFETIME = 600 ,
)
cors = CORS(app , resources = {r"/*" : {"origins" : "*" }})




@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(error):
  return render_template("404.html" , error = error)





class Dash_Page_Context(View):
   methods = ['GET']  
   def Render_Year(self):
        Current_Year = str(2025)
        return Current_Year

   def dispatch_request(self) -> str :
        CompanyID = "Osefa Homes & Developers "
        YEAR = self.Render_Year()
        if request.method == 'GET':
            return render_template('Home.html' , CompanyID = CompanyID  , YEAR = YEAR )
        else: 
            # Return requested profile thru client connect 
            return render_template('Home.html' , CompanyID = CompanyID , YEAR = YEAR  )
        

class Onboarding_Platform(View): 
    methods = ['GET', 'POST']  
    def dispatch_request(self) -> str :
        CompanyID = "Osefa Homes & Developers "
        if request.method == 'POST':
            EmailAddress = request.form.get("Email")
            Phone = request.form.get("Contact")
            Subject = """ Thank you for joining Osefa homes & Developers . You registered with phone [ {0} ] . Kindly usse that to log in """.format(Phone)
            Body = """ Welcome to Osefa Homes & Devs  """ 
            print(EmailAddress)
            print(Subject)
            base.Create_Email(EmailAddress , Subject , Body)
        else: 
            # Return requested profile thru client connect 
            return redirect('Home' , CompanyID = CompanyID , Info = Info  )



class Company_Contact_Profile(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self) -> str :
        CompanyID = "Osefa Homes & Developers "
        if request.method == 'POST':
            return render_template('contact.html' , CompanyID = CompanyID   )
        else: 
            # Return requested profile thru client connect 
            return render_template('contact.html' , CompanyID = CompanyID  )
        






app.add_url_rule('/', view_func=Dash_Page_Context.as_view('Home'))
app.add_url_rule('/contact/portal/', view_func=Company_Contact_Profile.as_view('Contact'))
app.add_url_rule('/portal/account/create/', view_func=Onboarding_Platform.as_view('join'))




if __name__=='__main__':
   app.run(host="0.0.0.0" , debug="False" )
