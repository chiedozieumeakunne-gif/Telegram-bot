#imports
import requests
import time
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(Path(__file__).parent/"key_card.env")

key_card = os.getenv("code")
offset = None
#Keyboard error handling
try:
 while True:
  try:
   #retrieving of data
   url = f"https://api.telegram.org/bot{key_card}/getUpdates"
   response = requests.get(url,  params = {"offset":offset, "timeout":30},timeout=40)
   
   data = response.json()
   print(data)
   #telegram error handling
   if not data.get("ok"):
     print("telegram error:",data.get("description"))
     time.sleep(5)
     continue

    #Processing of data
   for update in data["result"]:
     offset = update["update_id"] + 1
     message = update.get("message", {})
     text = message.get("text")
     print(text)

     if text.strip().lower() == "hello":
         url = f"https://api.telegram.org/bot{key_card}/sendMessage"
         letter = requests.post(url, data={
          "chat_id":7622104868, 
          "text":"how are you",})
     else:
          url = f"https://api.telegram.org/bot{key_card}/sendMessage"
          letter = requests.post(url, data={
          "chat_id":7622104868, 
          "text":"invalid",})
        
          print(text)
  except requests.exceptions.RequestException as e:     
    print(e)  

except KeyboardInterrupt :
  print("Error Code 402:Code Stopped ;)")




       



     
  
   

