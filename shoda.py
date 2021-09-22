from genericpath import exists
import shodan
import colorama
import sys , os
import json

from shodan.client import Shodan
cl = colorama.Fore.LIGHTCYAN_EX
cv = colorama.Fore.WHITE
rd = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
gn = colorama.Fore.GREEN

def banner():
    ban = """
 ___                    ___            _____               
| _ \___ _ __  __ ___ _| _ ) _____ __ |_   _|__ __ _ _ __  
|   / -_) '  \/ _` \ \ / _ \/ _ \ \ /   | |/ -_) _` | '  \ 
|_|_\___|_|_|_\__,_/_\_\___/\___/_\_\   |_|\___\__,_|_|_|_|                                                           
"""
    print (cl + ban)
    print (rd + "Created By Maximum Radikali ")
    print (yellow + "Channel : https://t.me/RemaxBoxTeam" + cv)
banner()
exist = os.path.exists("save.txt")
if exist == True:
    try:
        key = open("save.txt","r").read()
        ip = shodan.Shodan(key)
        target = str(input(gn + "please Enter IP Target -> " + cv))
        result = ip.host(target)
        data = json.dumps(result)
        sos = json.loads(data)
        print (gn + "Region Code -> " + str(sos['region_code']) + "\nIP -> "+str(sos['ip']) + "\npostal_code -> " +str(sos['postal_code']) + "\nCountry Code -> " + str(sos['country_code']) + "\nCity -> " + str(sos['city']) +  "\nasn -> " +str(sos['asn']) + "\nORG -> " + str(sos['org']) + "\nIP-Str -> " + str(sos['ip_str']) + "\nOS ->" + str(sos['os']) +  cv)
    except shodan.exception.APIError:
        print ("The Ip address invalid")

    
else:
    try:

        key = input(gn + "Please Enter API Key -> " + cv)
        test = shodan.Shodan(key)
        test.host("1.1.1.1")
        open("save.txt","w").write(key)
        target = input(yellow + "Please Enter Ip Target -> " + cv)
        ipp = shodan.Shodan(key)
        result = ipp.host(target)
        data = json.dumps(result)
        sos = json.loads(data)
        print (gn + "Region Code -> " + str(sos['region_code']) + "\nIP -> "+str(sos['ip']) + "\npostal_code -> " +str(sos['postal_code']) + "\nCountry Code -> " + str(sos['country_code']) + "\nCity -> " + str(sos['city']) +  "\nasn -> " +str(sos['asn']) + "\nORG -> " + str(sos['org']) + "\nIP-Str -> " + str(sos['ip_str']) + "\nOS ->" + str(sos['os']) +  cv)
        print (result)
    except:
        print ("Invalid Key , Please try again")



