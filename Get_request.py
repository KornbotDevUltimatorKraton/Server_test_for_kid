import json 
import requests 
list_web_status = {
  "statusCodes": {
    "200": "OK",
    "201": "Created",
    "204": "No Content",
    "400": "Bad Request",
    "401": "Unauthorized",
    "403": "Forbidden",
    "404": "Not Found",
    "500": "Internal Server Error"
  }
}

try:
   # Test getting real website check status 
   res = requests.get("https://examples.com")
   check_web_status = res.status_code
   print("Web status",check_web_status) 
   print("Status_meaning",list_web_status.get('statusCodes').get(str(check_web_status)))
except:
    print("You haven't connect to the internet or website is down") 

try:
   # Test getting the our own website test request 
   res_local_web  = requests.get("http://0.0.0.0:5789/")
   local_web = res_local_web.status_code
   print("Web status local ", local_web)
   print("Status_meaning",list_web_status.get('statusCodes').get(str(local_web)))
except:
    print("please run python3 server_test.py")
