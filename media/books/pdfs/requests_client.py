#client application -paytm
# requests - API consume
# pip intall requests
# 

import requests



GET_SINGL_DATA_URL = "http://127.0.0.1:8000/single_student/"

def get_single_data(id):
    res = requests.get(GET_SINGL_DATA_URL + str(id) + '/')
    print(res.json())

#get_single_data(1)     

GET_ALL_URL = "http://127.0.0.1:8000/all_student/"

def get_all_data():
    res = requests.get(GET_ALL_URL)
    print(res.content) # json data
    print(res.json())  #python dada

#get_all_data()   
headers = {'content-type':'application/json'}

API_URL = "http://127.0.0.1:8000/get_single_and_alldata/" 
API_CLASS_URL ="http://127.0.0.1:8000/Student-class-API/"  
API_URL_FUN ="http://127.0.0.1:8000/student_api/"

import json
def get_data(sid = None):
    data = {}
    if sid:
        data = {"id" : sid}
    json_data = json.dumps(data)  
    res = requests.get(API_URL_FUN ,headers=headers , data= json_data)
    print(res.json())

#get_data()    

def get_post(d): # to insert data in database
    
    #json_data =json.dumps(d)
    res = requests.post(API_URL_FUN ,headers=headers  , json=d)
    print(res.json())

di= {"name":"swapna" , "age":69, "city":"pune", "marks":108}
#get_post(di)


def get_put_update(data):   # to update data
    
    #json_data =json.dumps(d)
    #res = requests.patch(API_URL_FUN ,headers=headers   , json=data)
    res = requests.put(API_URL_FUN ,headers=headers   , json=data)
    print(res.json())

#dict= {"id": 29,"name":"OOOOOOOO" , "age":28, "city":"pune", "marks":88}
dict= {"id": 29,"city":"pune", "name":"IIIIII"}
#get_put_update(dict)

def delete_data(data):
    res = requests.delete(API_URL_FUN,headers=headers     , json=data)
    print(res.json())

dict = {"id":29}
delete_data(dict)     
