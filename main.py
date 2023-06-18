import typing as optional
from  fastapi import FastAPI,status,Response
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
from sqlalchemy.orm import sessionmaker
from prettytable import PrettyTable
from typing import List, Dict
from pydantic import BaseModel










app = FastAPI()

# class ServiceNumberEnum(str, Enum):
#     type1 = '1'
#     type2 = '3'
#     type3 = '5'
#
#
# @app.get('/BizagiServices/serviceNumber/{number}')
#
# def get_service_number(number:ServiceNumberEnum):
#     return {"Message":f"service number is {number}"}



# @app.get('/BizagiServices/GetFullname', status_code=status.HTTP_200_OK)
#
# def get_service_number(Name:str='mahyar',Family:str='razi' , response:Response=status.HTTP_200_OK):
#     if Name !='Mahyar':
#         response.status_code = status.HTTP_404_NOT_FOUND;
#     return {"Message":f"Your Name Is {Name} {Family}"}





#
# @app.get('/BizagiServices/GetFullname',tags=['name','family'], summary= "neahan dadne esm")
#
# def get_service_number(Name:str='mahyar',Family:str='razi'):
#     """
#     in api baraye namayesh name kamel hast
#
#     - **Name** "name khodeto vared kon"
#
#     - **Family** "family khodeto vared kon""
#
#     """
#
#     return {"Message":f"Your Name Is {Name} {Family}"}














# server = 'OKDC40024\NODE'
# database = 'dev_OKBPMS'
# username = 'App_bizagi'
# password = 'X6Wd5Ft5ekHdRW5A'
# driver = 'SQL Server'
#
# engine = create_engine(f'mssql://{username}:{password}@{server}/{database}?driver={driver}')
#
# base = declarative_base()
#
# season = sessionmaker(bind=engine)()
#
# products = season.query(CASESTATE).all()
# for product in products:
#     print(product.statuss)


#
#
# server = 'OKDC40024\\NODE'
# database = 'dev_OKBPMS'
# username = 'App_bizagi'
# password = 'X6Wd5Ft5ekHdRW5A'
# driver = 'SQL Server'
#
# # Create the connection string
# engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')
#
# try:
#     conn = engine.connect()
#     print("Connection successful!")
# except Exception as e:
#     print(f"Error: {str(e)}")

# mssql+pyodbc://@NEW-OFFICE\user/testdb?driver=ODBC Driver 17 for SQL Server

# result.append(string)

# Test the connection

class Item(BaseModel):
    coloumn1: str
    coloumn2: str=None
    coloumn3: str=None



@app.post('/BizagiServices/checkDuplicate')
def get_duplicated(items:List[Item]):
    result =[]
    count=0
    result = "false"
    for i in range(len(items)):
        string = items[i].coloumn1
        for j in range(len(items)):
            if items[i].coloumn1==items[j].coloumn1:
                count+=1
        if count>1:
            result="true"
        count =0

    return {"Is Duplicate":result}



#
# @app.get('/BizagiServices/GetFullname')
#
# def get_service_number(text1:str,text2:str,text3:str):
#     dataLists = [text1,text2,text3]
#
#     res= 'false'
#     for dataList in dataLists:
#         if text1==text2 or  text1==text3:
#             res = 'true'
#         if text1 == text2 or text2 == text3:
#             res = 'true'
#         if text1 == text3 or text2 == text3:
#             res = 'true'
#
#     if res=='true':
#         return {"Message":f"res is True"}
#     else:
#         return {"Message": f"res is false"}
