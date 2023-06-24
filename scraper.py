from urllib.request import urlopen
import bs4 as bs
import pandas as pd
import numpy as np 
import re
from datetime import date
def Extract_Date(Date_text):
    """Extracts date form various types of texts
        Arguments:
        Date_text:string
    Returns:
        Date
        
    """
    y=Date_text.text.split(":\xa0")[1].split("\n")[0].strip() #splits texts on \ and cleans up space and end of the line
    try: 
        return(dateutil.parser.parse(y)) # attmepts to parse it into a date 
    except:
        return(y)
         #\\to_do acctually handel the error instead of throughing it away 
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def get_Sudanbid():
    """
    """
    try :
        sudanbid_HTML=urlopen('https://www.sudanbid.com/') #gets sudan bid HTML
    except Exception as e:
        return "error reaching sudanbid" 
    #get items and link
    sudanbid_Soup=bs.BeautifulSoup(sudanbid_HTML,'html.parser')
    items=sudanbid_Soup.find_all('a','a_homelist') # beautifle soup find the tender titles taged as a_homelist
    sudanbid_list=[]#list to capture each element of the table 
    sudanbid_linklist=[]#list the links of each item 
    for tendor in items:
        sudanbid_list.append(tendor.get_text())
        sudanbid_linklist.append("https://www.sudanbid.com/"+tendor.attrs["href"])
    sudanbid_Df=pd.DataFrame(data=sudanbid_list,columns=["Itmes"])# creat and append into the 
    #get opening  dates
    sudanbid_Df["link"]=sudanbid_linklist
    open_dates=sudanbid_Soup.find_all(text=re.compile("Opening Date:"))# # beautifle soup find the tender opening date using regular expresion "Opening Date:" 
    sudanbid_list=[]
    for d in open_dates:
        sudanbid_list.append(Extract_Date(d))   
    sudanbid_Df["Opening Date"]=pd.to_datetime(sudanbid_list,errors='coerce')
    #get closing  dates
    close_dates=sudanbid_Soup.find_all(text=re.compile("Deadline:")) # beautifle soup find the tender opening date using regular expresion ""Deadline:"" 
    sudanbid_list=[]
    for d in close_dates:
        sudanbid_list.append(Extract_Date(d))   
    sudanbid_Df["Closeing Date"]= pd.to_datetime(sudanbid_list,errors='coerce')
    #get company 
    company=sudanbid_Soup.find_all("font",class_='sudanjob_orang_color') # beautifle soup find the tender posting form color // to do find a better way to do this 
    sudanbid_list=[]
    for i in company:
        sudanbid_list.append(i.get_text())   
    sudanbid_Df["company"]=sudanbid_list
    # filter active tendors
    active_mask= (sudanbid_Df["Closeing Date"] >= np.datetime64('today'))  
    return sudanbid_Df[active_mask]
print(get_Sudanbid().to_excel(r"sudanbid.xlsx"))

