# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:14:38 2021

@author: Isaac.C
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:06:29 2021

@author: Isaac.C
"""

import urllib.parse
import requests
main_api="https://www.mapquestapi.com/directions/v2/route?"
#orig="Quito"
#dest="Guayaquil"
key="357ZMH4n7FKnkNJ08roxGkPUbGSuVrd5" #acceder ea todo el contenido que tien

while True:
    orig=input("locacion de inicio: ")
    if orig=="quit" or orig=="q":
        break
    dest=input("Destino: ")
    if dest=="quit" or dest=="q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data=requests.get(url).json()
    json_status=json_data["info"]["statuscode"]

    if json_status == 0:
        print("API status: " + str(json_status)+"=A successful router call. \n")
        print("Direction froms"+(orig)+"to"+(dest))
        print("Trip duration:  "+(json_data["route"]["formattedTime"]))
        print("kilometros:         " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel (Litros):         " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"])+"("+str("{:.2f}".format((each["distance"])*1.61)+"km)"))
        print("===========================================================\n")
    elif json_status==402:
        print("***********************************************************")
        print("For status code: "+ str(json_status)+"; Invalid user inputs for one or both locations.")
        print("***********************************************************\n")
        print("===========================================================")
    else:
        print("\n***********************************************************")
        print("Status code: "+ str(json_status)+"; Refer to:")
        print("https://developer.mopquest.com/documentation/directions-api/status-codes")
        print("***********************************************************\n")
        
    
    