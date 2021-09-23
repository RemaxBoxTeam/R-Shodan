from genericpath import exists
import shodan
import colorama
import sys , os
import json
import socket
#socket.gaierror:

from shodan.client import Shodan
cl = colorama.Fore.LIGHTCYAN_EX
cv = colorama.Fore.WHITE
rd = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
gn = colorama.Fore.GREEN
hv = colorama.Fore.LIGHTMAGENTA_EX

def banner():
    ban = """
 ___                    ___            _____               
| _ \___ _ __  __ ___ _| _ ) _____ __ |_   _|__ __ _ _ __  
|   / -_) '  \/ _` \ \ / _ \/ _ \ \ /   | |/ -_) _` | '  \ 
|_|_\___|_|_|_\__,_/_\_\___/\___/_\_\   |_|\___\__,_|_|_|_|                                                           
"""
    print (cl + ban)
    print (rd + "Created By Maximum Radikali ")
    print (yellow + "Channel : https://t.me/RemaxBoxTeam\n\n" + cv)
banner()
selector = input(rd + "1-GetIPAddressFromUrl\n2-Shodan\n" + cl + "Please Select an Option --> " + cv)
if selector == "1":
    try:

    
        print (hv + "You Selected First Option :) \n\n")
        site = input("Please Enter the URL -> " + cv)
        result = socket.gethostbyname(site)
        print (rd + "The IP Address is : " +result + "\nSite : " +  site + cv)
    except socket.gaierror:
        print (hv + "Please Enter Correct URL \n " + gn + "EX : www.example.com" + cv)
elif selector == "2":
    print (hv + "You Selected The Second Option :) \n \n")
    exist = os.path.exists("save.txt")
    if exist == True:
        try:
            key = open("save.txt","r").read()
            ip = shodan.Shodan(key)
            target = str(input(gn + "please Enter IP Target -> " + cv))
            result = ip.host(target)
            data = json.dumps(result)
            sos = json.loads(data)
            print (gn + "Region Code -> " + str(sos['region_code']) + "\nIP -> "+str(sos['ip']) + "\npostal_code -> " +str(sos['postal_code']) + "\nCountry Code -> " + str(sos['country_code']) + "\nCity -> " + str(sos['city']) +  "\nasn -> " +str(sos['asn']) + "\nORG -> " + str(sos['org']) + "\nIP-Str -> " + str(sos['ip_str']) + "\nOS -> " + str(sos['os']) +  cv)
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
            print (gn + "Region Code -> " + str(sos['region_code']) + "\nIP -> "+str(sos['ip']) + "\npostal_code -> " +str(sos['postal_code']) + "\nCountry Code -> " + str(sos['country_code']) + "\nCity -> " + str(sos['city']) +  "\nasn -> " +str(sos['asn']) + "\nORG -> " + str(sos['org']) + "\nIP-Str -> " + str(sos['ip_str']) + "\nOS -> " + str(sos['os']) +  cv)
        except:
            print ("Invalid Key , Please try again")



