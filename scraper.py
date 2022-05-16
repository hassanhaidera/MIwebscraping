from urllib.request import urlopen
import bs4 as bs
import pandas as pd
def get_Sudanbid():
    """"
    """
    try :
        sudanbid_HTML=urlopen('https://www.sudanbid.com/') #gets sudan bid HTML
    except Exception as e:
        return "error reaching sudanbid" 
    sudanbid_Soup=bs.BeautifulSoup(sudanbid_HTML,'html.parser').find_all('a','a_homelist') # beautifle soup find the tender titles taged as a_homelist
    sudanbid_list=[]#list to capture each element of the table 
    for tendor in sudanbid_Soup:
        sudanbid_list.append(tendor.get_text())
    sudanbid_Df=pd.DataFrame(data=sudanbid_list,columns=["Itmes"])
    sudanbid_list=[]
    return sudanbid_Df
print(get_Sudanbid())