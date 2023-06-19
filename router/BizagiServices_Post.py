from fastapi import APIRouter
from  fastapi import FastAPI,status,Response
from typing import List, Dict
from pydantic import BaseModel



router = APIRouter(prefix='/bizagiServices_Post')

class Item(BaseModel):
    coloumn1: str
    coloumn2: str=None
    coloumn3: str=None



@router.post('/checkDuplicate', tags=['Post'])
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
    return {"Is Duplicate" : f"{result}"}
