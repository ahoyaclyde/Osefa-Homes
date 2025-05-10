import sqlite3
from sqlite3 import Error
from flask import *
import os 

app=Flask(__name__)

DatabaseURL = os.path.join(app.root_path , "") + "/database/OsefaHomes.db"
app.config['DatabaseURL']= DatabaseURL

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn




### Clientelle_CHarter Block 
### COntrollers 



def Create_Account(Property):
    """
    Create a new PropertyName into the PropertyNames table
    :param conn:
    :param PropertyName:
    :return: PropertyName id
    """
    conn = create_connection(DatabaseURL)
    with app.app_context():
        
        sql = '''INSERT INTO Clientelle(ClientToken , EmailAddress , Fullname , Phone , SecureString , CreationDate , CreationTime , AccountType , IsExistent  )
            VALUES(?,?,?,?,?,?,?,?,0) '''
        cur = conn.cursor()
        cur.execute(sql,Property)
        conn.commit()
        conn.close()
        return "Success"
    


## Return Available User Profiles 

	

def Print_Clientelle_Listings(AccountType):
    if not AccountType:
        AccountType = "Standard"
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Clientelle Where AccountType = ? " , (AccountType,))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return (DatabaseFeed)



def Print_Profile_States(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Clientelle Where IsExistent = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return (DatabaseFeed)



def Print_Profile_Username(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT Fullname FROM Clientelle Where Phone = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return str(DatabaseFeed).strip("[]()'',")



def Print_Profile_Block(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Clientelle Where Phone = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return (DatabaseFeed)



def Account_IsExistent(Bindings):
    """
    Query all DataItem in the Clientelle_Pool ss table
    :param conn: the Connection object
    :return:
    """
    
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT EmailAddress FROM CommunityCharter ")

    DataItem = cur.fetchall()

    for bit in DataItem:
        print(bit)
    return DataItem





def Confirm_Address_Key(conn, Bindings):
    """
    Query Clientelless by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT Phone FROM Clientelle WHERE Phone = ?", (Bindings,))

    DataItem = cur.fetchall()

    for bit in DataItem:
        print(bit)

        return str(DataItem).strip("()[]'',");\


def Confirm_Access_Token(conn, Bindings):
    """
    Query Clientelless by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
 
    cur = conn.cursor()
    cur.execute("SELECT SecureString FROM Clientelle WHERE SecureString =?", (Bindings,))

    DataItem = cur.fetchall()

    for bit in DataItem:
        print(bit)

        return DataItem;



### Clientelle_CHarter Block 
### COntrollers 



def Create_Invoice(Property):
    """
    Create a new PropertyName into the PropertyNames table
    :param conn:
    :param PropertyName:
    :return: PropertyName id
    """
    conn = create_connection(DatabaseURL)
    with app.app_context():
        
        sql = '''INSERT INTO Invoices (InvoiceID , BilledTo , ProjectID , MiddleMan , InvoiceType , CreationTime , CreationDate  , GrossAmount , ExpiresOn  , IsExistent)
            VALUES(?,?,?,?,?,?,?,?,?,0) '''
        cur = conn.cursor()
        cur.execute(sql,Property)
        conn.commit()
        conn.close()
        return "Success"
    


def Print_Invoices(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Invoices Where IsExistent = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return DatabaseFeed



def Print_Invoice_By_Ownership(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Invoices Where BilledTo = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return (DatabaseFeed)




def Print_Invoice_By_ProjectID(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Invoices Where ProjectID = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return (DatabaseFeed)



def Print_Invoice_By_Type(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Invoices Where InvoiceType = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return (DatabaseFeed)



def Print_Invoice_By_Expiration(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Invoices Where ExpiresOn = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return (DatabaseFeed)




### Projects_CHarter Block 
### Projects 



def Create_Project(Property):
    """
    Create a new PropertyName into the PropertyNames table
    :param conn:
    :param PropertyName:
    :return: PropertyName id
    """
    conn = create_connection(DatabaseURL)
    with app.app_context():
        
        sql = '''INSERT INTO Projects (ProjectID , ProjectOwner ,Description , AreaCode  , Commence , Ending , CreationDate , CreationTime , GrossAmount , Middleman , IsExistent)
            VALUES(?,?,?,?,?,?,?,?,?,?,0) '''
        cur = conn.cursor()
        cur.execute(sql,Property)
        conn.commit()
        conn.close()
        return "Success"
    






def Print_Projects(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Projects Where IsExistent = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return DatabaseFeed


def Print_Project_By_Ownership(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Projects Where ProjectOwner = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(str(DataChunk))
    return  DatabaseFeed




### Mail_CHarter Block 
### Emails 



def Create_Mail(Property):
    """
    Create a new PropertyName into the PropertyNames table
    :param conn:
    :param PropertyName:
    :return: PropertyName id
    """
    conn = create_connection(DatabaseURL)
    with app.app_context():
        
        sql = '''INSERT INTO Mail (MailID , Receiver , Subject , Description , MiddleMan , CreationTime , CreationDate ,  IsExistent)
            VALUES(?,?,?,?,?,?,?,0) '''
        cur = conn.cursor()
        cur.execute(sql,Property)
        conn.commit()
        conn.close()
        return "Success"
    





def Print_Mail_List():
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Projects"     )

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return DatabaseFeed





### Projects_CHarter Block 
### Projects 



def Create_Subscriber(Property):
    """
    Create a new PropertyName into the PropertyNames table
    :param conn:
    :param PropertyName:
    :return: PropertyName id
    """
    conn = create_connection(DatabaseURL)
    with app.app_context():
        
        sql = '''INSERT INTO Subscribers (SubId , SubsFullname , SubsContact , SubsEmail, CreationDate , CreationTime , IsExistent )
            VALUES(?,?,?,?,?,?,0) '''
        cur = conn.cursor()
        cur.execute(sql,Property)
        conn.commit()
        conn.close()
        return "Success"
    






def Print_Subscribers(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Subscribers Where IsExistent = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return DatabaseFeed




def Print_Subscribers_Contacts(Bindings):
  
      
    """
    Query all DatabaseFeed in theProperty_Schema table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection(DatabaseURL)
    cur = conn.cursor()
    cur.execute("SELECT SubsContact FROM Subscribers Where IsExistent = ? " , ( Bindings , ))

    DatabaseFeed = cur.fetchall()

    for DataChunk in DatabaseFeed:
        print(DataChunk)
    return DatabaseFeed




Property = ("84989839" , "ahoyaclyde@gmail.com" , "Clydenso Dela gaza" , "0724534645",  "Ferociuos23" , "3/4/2012" , "12:53 pm " , "Administrator" , "0")
#Create_Account(Property)
#Print_Clientelle_Listings("Administrator")

#Invoice = ("DR23-239" , "Maria Sten" , "RTY-453-33" , "Administrator" , "Mpesa" , "12:34 am" , "4/3/2025" , "3450000" ,  "4/3/2026" )
#Create_Invoice(Invoice)


#Project = ("#DFR-34232"  , "AhoyaClyde" , "Contemporary Dsign" ,  "Busia" , "2/4/2025" , "14/4/2025" , "3/4/2012" , "12:53 pm " , "45000000" , "Farjalla Diciye" )
#Create_Project(Project)



#Mails  = ("RTY-342323" , "ahoyaclyde@gmail.com" , "Come here Now " , "Could you come outside the house " , "Farjalla" ,  "3:49:34 PM " , "4/2/2025" )
#Create_Mail(Mails)


#Subscriber = ("GKE-34343", "Clyde Javis" , "0724353242" , "ahoyaclyde@gmail.com" , "3/4/35" , "4:20 AM"  )
#Create_Subscriber(Subscriber)