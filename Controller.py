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
import Intercom_Connector as control_baselink
from utils import base as base_controller
#from flask_sslify import SSLify

from utils import base as base 

#import Twilio_Content_Provider as Twilio_Service
app=Flask(__name__)
#sslify = SSLify(app)
app.config.update(
    PERMANENT_SESSION_LIFETIME = 600 ,
)
cors = CORS(app , resources = {r"/*" : {"origins" : "*" }})



DatabaseUrl = os.path.join(app.root_path , "") + "database/OsefaHomes.db"
app.config['DatabaseUri']= DatabaseUrl

# Erro Handler Protocol Environs 
# Auto Redirect To 404.Html 
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(error):
  return render_template("404.html" , error = error)


CompanyID = "Osefa Homes "
AbstractSequences = ["DateStr" , "TimeStr"]

def Render_Abstract_Time():
    return base_controller.Space_Time_Generator(AbstractSequences[-1])

# Base Route Address For Home/Landing Page Scenarios 
# Initial Page 
class Dash_Page_Context(View):
   methods = ['GET']  
   def Render_Year(self):
        Current_Year = str(2025)
        return Current_Year

   def dispatch_request(self) -> str :
        UID = base_controller.Construct_String_Address(8)
        YEAR = self.Render_Year()
        if request.method == 'GET':
            return render_template('Home.html' , CompanyID = CompanyID  , YEAR = YEAR , UID = UID  )
        else: 
            # Return requested profile thru client connect 
            return render_template('Home.html' , CompanyID = CompanyID , YEAR = YEAR , UID = UID   )
        

# Subscriber Model Onboarding 
# Intergrates Clients To Customer Base List  
# Should Have A Db Impl of Storing  Reg - Subscribers 
class Onboarding_Platform(View): 
    methods = ['GET', 'POST']  

    def dispatch_request(self) -> str :
      
        CreationDate = base_controller.Space_Time_Generator("DateStr")
        CreationTime = base_controller.Space_Time_Generator("TimeStr")
        Info = "SuccessFull"
        if request.method == 'POST':
            SubsData  = list(request.form.values())
            SubsData.append(CreationDate)
            SubsData.append(CreationTime)
            control_baselink.Create_Subscriber(SubsData)
            EmailAddress = request.form.get("Email")
            Phone = request.form.get("Contact")
            Subject = """ Thank you for joining Osefa homes & Developers . You registered with phone [ {0} ] . Kindly usse that to log in """.format(Phone)
            Body = """ Welcome to Osefa Homes & Devs  """ 
            print(EmailAddress)
            print(Subject)
            base.Create_Email(EmailAddress , Subject , Body)
            return redirect(url_for('Home' , CompanyID = CompanyID , Info = Info  ))

        else: 
            # Return requested profile thru client connect 
            return redirect(url_for('Home' , CompanyID = CompanyID , Info = Info  , ))



# Contact Us Master Form Submission Protocol
# Relays Feedback Thru Email After Supply Of Neck Creds

class Contact_Us(View): 
    methods = ['GET', 'POST']  
    def dispatch_request(self) -> str :
       
        if request.method == 'POST':
            EmailAddress = request.form.get("Email")
            Phone = request.form.get("Contact")
            Subject = request.form.get("Subject")
            Subject =Subject + str("Sender Contact -") + Phone  
          
            Message = request.form.get("Message")
         
            base.Create_Email(EmailAddress , Subject , Message)
        else: 
            # Return requested profile thru client connect 
            return redirect('Home' , CompanyID = CompanyID , Info = Info  )



# Base Route Address For Contact Page Scenarios 
# Independent Page Route
 
class Company_Contact_Profile(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self) -> str :
        Abstract = Render_Abstract_Time
       
        if request.method == 'POST':
            return render_template('contact.html' , CompanyID = CompanyID  , Abstract = Abstract )
        else: 
            # Return requested profile thru client connect 
            return render_template('contact.html' , CompanyID = CompanyID  , Abstract = Abstract  )
        




 
class Admin_Controller_Interface(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self) -> str :
       
        if request.method == 'GET':
            Indicator = int(0) 
            Indicator_Next = int(1)  
            Clientelle_Profiles = control_baselink.Print_Clientelle_Listings("Standard") 
            Inactive_Profiles = control_baselink.Print_Profile_States(Indicator)
            #Checks 
            if Clientelle_Profiles:
                Clientelle_Index = len(Clientelle_Profiles)
            else:
                Clientelle_Index = int(0) 

            Invoiced_Profiles = control_baselink.Print_Invoices(Indicator)
            Pending_Profiles  = control_baselink.Print_Invoices (Indicator_Next)
            #Checks 
            if Invoiced_Profiles:
                Invoice_Index = len(Invoiced_Profiles)
            else:
                Invoice_Index = int(0) 


            # Check For Pending Profiles 
            if Pending_Profiles: 
                Pending_Index = len(Pending_Profiles)
            else:
                Pending_Index = int(0)

            Projects = control_baselink.Print_Projects(Indicator)
        
            if (Projects):
                Project_Index = len(Projects)
            else:
                Project_Index = int(0)

            Sub_Profiles =  control_baselink.Print_Subscribers(Indicator)

            if Sub_Profiles : 
                Sub_Index = len(Sub_Profiles)
            else:
                Sub_Index = int(0)

            
            
 
            return render_template('Admin-Controller-Concept.html' , CompanyID = CompanyID , Clientelle_Index = Clientelle_Index , Clientelle_Profiles = Clientelle_Profiles , Invoice_Index = Invoice_Index , Pending_Profiles = Pending_Profiles , Pending_Index  =  Pending_Index ,  Project_Index = Project_Index , Sub_Index = Sub_Index  )
        else: 
            # Return requested profile thru client connect 
            return render_template('Admin-Controller-Concept.html' , CompanyID = CompanyID  )




class Admin_Invoice_Interface(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self) -> str :
       
        if request.method == 'GET':
            Indicator = int(0)  
            Invoiced_Profiles = control_baselink.Print_Invoices(Indicator)
            #Checks 
            if Invoiced_Profiles:
                Invoice_Index = len(Invoiced_Profiles)
            else:
                Invoice_Index = int(0) 
 
            return render_template('Admin-Collative-Invoice.html' , CompanyID = CompanyID , Invoiced_Profiles = Invoiced_Profiles , Invoice_Index = Invoice_Index )
        else: 
     

            # Return requested profile thru client connect 
            return render_template('Admin-Collative-Invoice.html' , CompanyID = CompanyID  )
        
        




class Admin_Clientelle_Interface(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self) -> str :
       
        if request.method == 'GET':
            Indicator = int(1) 
            Indicator_Next = int(0)  
            Clientelle_Profiles = control_baselink.Print_Clientelle_Listings("Standard") 
            Inactive_Profiles = control_baselink.Print_Profile_States(Indicator)
            #Checks 
            if Clientelle_Profiles:
                Clientelle_Index = len(Clientelle_Profiles)
            else:
                Clientelle_Index = int(0) 
 
            if Inactive_Profiles :
                Inactive_Index  = len(Inactive_Profiles)
            else:
                Inactive_Index  = int(0) 
            
            return render_template('Admin-User-Concept.html' , CompanyID = CompanyID , Clientelle_Profiles = Clientelle_Profiles , Clientelle_Index = Clientelle_Index , Inactive_Index  = Inactive_Index  , Inactive_Profiles = Inactive_Profiles  )
        else: 
            # Return requested profile thru client connect 
            return render_template('Admin-User-Concept.html' , CompanyID = CompanyID  )
        




class Admin_Project_Interface(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self) -> str :
        Indicator = int(0) 
        Indicator_Next = int(1) 
       
        if request.method == 'GET':
            Projects  = control_baselink.Print_Projects(Indicator)
            Stale_Projects = control_baselink.Print_Projects(Indicator_Next)
        
            if (Projects):
                Project_Index = len(Projects)
            else:
                Project_Index = int(0)


            if (Stale_Projects):
                Stale_Index = len(Stale_Projects)
            else:
                Stale_Index = int(0)


            return render_template('Admin-Projects-Concept.html' , CompanyID = CompanyID , Projects = Projects , Project_Index = Project_Index , Stale_Projects = Stale_Projects , Stale_Index = Stale_Index )
        else: 
            # Return requested profile thru client connect 
            return render_template('Admin-Projects-Concept.html' , CompanyID = CompanyID  )
        
class Mail_List_Interface(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self) -> str :
       
        if request.method == 'GET':
            MailProfiles =  control_baselink.Print_Mail_List()

            if MailProfiles : 
                MailIndex = len(MailProfiles)
            else:
                MailIndex = int(0)

            return render_template('Mail-List-Concept.html' , CompanyID = CompanyID , MailProfiles = MailProfiles , MailIndex = MailIndex  )
        else: 
            # Return requested profile thru client connect 
            return render_template('Mail-List-Concept.html' , CompanyID = CompanyID  )


   
class Subscriber_Array_Interface(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self) -> str :
       
        Indicator = int(0)
        if request.method == 'GET':
            
            Sub_Profiles =  control_baselink.Print_Subscribers(Indicator)

            if Sub_Profiles : 
                Sub_Index = len(Sub_Profiles)
            else:
                Sub_Index = int(0)

            

            return render_template('Subscriber-Array-Concept.html' , CompanyID = CompanyID , Sub_Profiles = Sub_Profiles , Sub_Index = Sub_Index  )
        else: 
               
            # Return requested profile thru client connect 
            return render_template('Subscriber-Array-Concept.html' , CompanyID = CompanyID  )
        
        


class Authenticator_Concept(View):
    methods = ['GET', 'POST']
    def dispatch_request(self) -> list :
        Connection_Manager =control_baselink.create_connection(DatabaseUrl)
        if request.method == 'POST':
                # - Action Zone
                Credentials = request.form
                PhoneTag = request.form.get("Contact")
                # Database Profiling
                SecureString = request.form.get("Credentials")
                PhoneTag_Captcha =  control_baselink.Confirm_Address_Key(Connection_Manager, PhoneTag)
                Crypto_Captcha =  control_baselink.Confirm_Access_Token(Connection_Manager, SecureString)
                print( PhoneTag_Captcha)
                if(PhoneTag == "0741371429"):
                    if(SecureString == "Admin"):
                        return redirect(url_for('Admin'))
                    else:
                        if ( PhoneTag_Captcha != None ):
                            if(Crypto_Captcha != None):
                                return redirect(url_for("Dashboard" ,AccountHolder = PhoneTag   ))
                            else:

                                return redirect(url_for('Auth'))
                        else:

                            return redirect(url_for('Auth'))
                else:
                    return render_template("Auth.html")
        return render_template("Auth.html")


class Account_Creator_Concept(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        
        Connection_Manager =control_baselink.create_connection(DatabaseUrl)
        UID = base_controller.Construct_String_Address(10)
        CreationDate = base_controller.Space_Time_Generator("DateStr")
        CreationTime = base_controller.Space_Time_Generator("TimeStr")
        
        if request.method == 'POST':
            ProfileInformation = request.form
            for Profile in ProfileInformation.values(): 
                print(Profile)
          
            # Appending The 'Active Tag ' Done to remove db locked error 
            # improper referencing was blocking read/write to support user serialization 
            DataBank = list(request.form.values())
            control_baselink.Create_Account(DataBank)
        # Return requested profile thru client connect 
        return render_template('CreateAccount.html' , CompanyID = CompanyID , UID = UID , CreationTime = CreationTime , CreationDate = CreationDate   )

        
class Clientelle_Relay_Interface(View):
   methods = ['GET', 'POST']  
   def dispatch_request(self , AccountHolder) -> str :
        Profile_Username = control_baselink.Print_Profile_Username(AccountHolder)
        User_Profile_Block = control_baselink.Print_Profile_Block(AccountHolder)
        if(User_Profile_Block):
            if request.method == 'GET':
                if(Profile_Username):
                    print(Profile_Username)
                    Projects_Profiles =  control_baselink.Print_Project_By_Ownership(Profile_Username)

                if Projects_Profiles : 
                    Projects_Index = len(Projects_Profiles)
                else:
                    Projects_Index = int(0)



                return render_template('Clientelle_Relay_Dash.html' , CompanyID = CompanyID , Projects_Profiles = Projects_Profiles, Projects_Index = Projects_Index , User_Profile_Block = User_Profile_Block  )
             
        # Return requested profile thru client connect 
        return render_template('Clientelle_Relay_Dash.html' , CompanyID = CompanyID  )



class Mass_Mail_Dispatch(View):
   methods = ['POST']  
   def dispatch_request(self) -> str :
       
        if request.method == 'POST':
            Indicator = int(0)  
            Topicline = request.form.get("Subject")
            SubjectMatter  = request.form.get("Matter")
            Subs_Profiles = control_baselink.Print_Subscribers_Contacts(Indicator)
            #Checks 
            if Subs_Profiles:
                print(Subs_Profiles)
                for Profile in Subs_Profiles: 
                    print(Profile)
                    base_controller.Create_Email(Profile , Topicline , SubjectMatter )
            else:
                return redirect(url_for('Subscribe'))  

        # Return requested profile thru client connect 
        return redirect(url_for('Subscribe'))        

app.add_url_rule('/', view_func=Dash_Page_Context.as_view('Home'))
app.add_url_rule('/contact/portal/', view_func=Company_Contact_Profile.as_view('Contact'))
app.add_url_rule('/portal/account/create/', view_func=Onboarding_Platform.as_view('join'))
app.add_url_rule('/portal/account/contact-us/', view_func=Contact_Us.as_view('Contact-Osefa'))
app.add_url_rule('/Home/Administrator/Dashboard/', view_func=Admin_Controller_Interface.as_view('Admin'))

app.add_url_rule('/Home/Administrator/Mail/Mass/Dispatch/', view_func=Mass_Mail_Dispatch.as_view('MassDispatch'))
app.add_url_rule('/Home/Administrator/Dashboard/Clientelle/', view_func=Admin_Clientelle_Interface.as_view('Clientelle'))
app.add_url_rule('/Home/Administrator/Dashboard/Invoice/', view_func=Admin_Invoice_Interface.as_view('Invoice'))
app.add_url_rule('/Home/Administrator/Dashboard/Projects/', view_func=Admin_Project_Interface.as_view('Projects'))
app.add_url_rule('/Auth/', view_func=Authenticator_Concept.as_view('Auth'))
app.add_url_rule('/Create/Account/', view_func=Account_Creator_Concept.as_view('CreateAccount'))
app.add_url_rule('/Home/Administrator/Mail/List/', view_func=Mail_List_Interface.as_view('Mail'))
app.add_url_rule('/Home/Administrator/Subscribers/Listings/', view_func=Subscriber_Array_Interface.as_view('Subscribe'))
app.add_url_rule('/Home/Clientelle/Accounts/<string:AccountHolder>/Dashboard/', view_func=Clientelle_Relay_Interface.as_view('Dashboard'))


if __name__=='__main__':
   app.run(host="0.0.0.0" , debug="False" )
