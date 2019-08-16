# App Backend
import sqlite3
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def ImportData():
    filename = filedialog.askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    con = sqlite3.connect('Database.db')
    wb = pd.read_excel(filename,sheet_name=None) 
    for sheet in wb:
        wb[sheet].to_sql(sheet,con,index =False,if_exists='replace')
        con.commit()
    con.close()  
    messagebox.showinfo('Import Data From Excel','Data has imported Successfully !')    # Display a message box when data has impoted successfully into sqlite3 database.
        

def Display(sso):
    con = sqlite3.connect('Database.db')
    cur = con.cursor()
    cur.execute(f'SELECT Employee_Name,GE_Sponser,GE_Business,L1_Genpact_MGr,L2_Genpact_MGr,L3_Genpact_MGr   FROM Data WHERE Contractor_SSO_ID = {sso}')
    rec = cur.fetchall()
    return rec
    
  

