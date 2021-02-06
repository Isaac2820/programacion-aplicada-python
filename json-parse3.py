#ENTRADAS DADAS POR EL USUARIO 
import  urllib.parse
import requests
main_api="https://www.mapquestapi.com/directions/v2/route?"
key="357ZMH4n7FKnkNJ08roxGkPUbGSuVrd5"

while True: 
    orig=input('ubicacion inicial: ')
    dest=input('destino: ')
    url= main_api+ urllib.parse.urlencode({"key": key,"from":orig,"to":dest})
    print("URL: "+(url)) 
    
    json_data=requests.get(url).json()
    json_status=json_data["info"]["statuscode"]
    
    if json_status==0:
        print("API Status: " + str(json_status)+ " = A successfull route call.\n")
