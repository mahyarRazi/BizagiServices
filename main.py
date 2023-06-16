import typing as optional
from  fastapi import FastAPI,status,Response
from enum import Enum

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










@app.get('/BizagiServices/GetFullname',tags=['name','family'], summary= "neahan dadne esm")

def get_service_number(Name:str='mahyar',Family:str='razi'):
    """
    in api baraye namayesh name kamel hast

    - **Name** "name khodeto vared kon"

    - **Family** "family khodeto vared kon""

    """

    return {"Message":f"Your Name Is {Name} {Family}"}