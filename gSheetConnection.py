import pandas as pd
import numpy as np
import traceback # for error handling
import logging # for error handling
from oauth2client.service_account import ServiceAccountCredentials # for authntication  
import gspread #API for Google Sheets
from df2gspread import df2gspread as d2g #Transfer data between Google Spreadsheets and Pandas DataFrame.
df=pd.DataFrame(np.random.rand(10,5),columns=[f"C{i}" for i in range(1,6)])
spreadsheet_key = '1XhGDS2jepGXgxCkuCrCY7lwOliDRhQRBucUU8vIcZVE'# book name
def send2sheet(sheet_key,dataframe):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive'
             ]# setting scope for sheets and google API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'miwebscraping-c65325ff0bee.json', scope)# service account credtions for account tendor@miwebscraping.iam.gserviceaccount.com
    wks_name = 'Sheet1'#sheet name 
    try :
        d2g.upload(dataframe, sheet_key, wks_name, credentials=credentials, row_names=True)
        return "uploaded with no issue"
    except Exception  as e :
        return e
x=send2sheet(spreadsheet_key,df)
print(x)

