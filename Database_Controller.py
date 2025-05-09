import sqlite3 , os 
from flask import *
from sqlite3 import Error
import uuid


app=Flask(__name__)
def create_connection(db_file):
    """ create a database connection to the DFIite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, Create_DB_Schema):
    try:
        c = conn.cursor()
        c.execute(Create_DB_Schema)
    except Error as e:
        print(e)

def Unbox_Database_Scheme(DatabaseURL):
   

    # Usermode  - Represents the user's housing  status wether hes searching . looking , booking 
    # Override @ Init - Use Default constructors if user is absent from zoning() 
    # Protocol - For LoggedIN | LoggedOUT Conditions 

    Clientelle_Schema = """CREATE TABLE IF NOT EXISTS Clientelle (
                                    ClientToken text UNIQUE  NOT NULL,
                                    EmailAddress text NOT NULL,
                                    Fullname text NOT NULL ,
                                    Phone text NOT NULL ,
                                    SecureString text NOT NULL ,
                                    CreationDate text NOT NULL,
                                    CreationTime text NOT NULL,
                                    AccountType integer NOT NULL ,
                                    IsExistent integer NOT NULL 
                                    
                                    
                                );"""


    Projects_Schema = """CREATE TABLE IF NOT EXISTS  Projects (
                                    ProjectID integer UNIQUE  NOT NULL ,
                                    ProjectOwner text  NOT NULL,
                                    Description text NOT NULL,
                                    AreaCode text NOT NULL,
                                    Commence text NOT NULL ,
                                    Ending text NOT NULL ,
                                    CreationDate text NOT NULL,
                                    CreationTime  text NOT NULL , 
                                    GrossAmount integer NOT NULL ,
                                    Middleman text NOT NULL , 
                                    IsExistent integer NOT NULL 

                                    
                                );"""





    Invoice_Schema = """CREATE TABLE IF NOT EXISTS Invoices (
                                    InvoiceID  text NOT NULL ,
                                    BilledTo text NOT NULL , 
                                    ProjectID text NOT NULL , 
                                    MiddleMan text NOT NULL ,
                                    InvoiceType text NOT NULL ,
                                    CreationTime text NOT NULL ,
                                    CreationDate text NOT  NULL , 
                                    GrossAmount text NOT NULL , 
                                    ExpiresOn text NOT NULL , 
                                    IsExistent interger NOT NULL 
                                  
                                );"""


    Transactional_Schema = """CREATE TABLE IF NOT EXISTS Transactions (
                                    TransactionID text NOT NULL ,
                                    Issuer text NOT NULL , 
                                    ReceivedBy text NOT NULL ,
                                    Platform  text NOT NULL ,
                                    GrossAmount interger NOT NULL ,
                                    CreationTime text NOT NULL , 
                                    CreationDate text NOT NULL ,
                                    Reference text NOT NULL , 
                                    BalanceOf text NOT NULL ,
                                    IsExistent integer NOT NULL 
                                    

                                    
                                );"""





    InMail_Schema = """CREATE TABLE IF NOT EXISTS Mail (
                                    MailID text NOT NULL ,
                                    Receiver text NOT NULL ,
                                    Subject text NOT NULL ,
                                    Description text NOT NULL , 
                                    MiddleMan text NOT NULL ,
                                    CreationTime text NOT NULL , 
                                    CreationDate  text NOT NULL , 
                                    IsExistent integer NOT NULL 
                                    

                                    
                                    
                                );"""


    Subscribers_Schema = """CREATE TABLE IF NOT EXISTS Subscribers (
                                SubID text NOT NULL ,
                                SubsFullname text NOT NULL , 
                                SubsContact text NOT NULL,
                                SubsEmail text NOT NULL , 
                                CreationDate text NOT NULL , 
                                CreationTime text NOT NULL , 
                                IsExistent integer NOT NULL 
                    
                                
                            );"""    


                                            


    # create a database connection
    conn = create_connection(DatabaseURL)


# create tables
    if conn is not None:
        # Create Clientelle Table Structure 
        # Hold User Information Here
        create_table(conn, Clientelle_Schema)

        # Create Property Table Structure 
        # Hold Property Information Here
        create_table(conn,  Projects_Schema)

        create_table(conn , Transactional_Schema)

        create_table(conn , Invoice_Schema)

        create_table(conn , InMail_Schema)

       
        create_table(conn , Subscribers_Schema)
    else:
        print("Creation Of [Osefa] Database Has Failed .")
        print("The Process Ended With The Following Results : ")


Unbox_Database_Scheme(os.path.join(app.root_path , "database/OsefaHomes.db"))