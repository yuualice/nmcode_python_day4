import os
import requests
from time import sleep

def is_legit(url):
  try:
    if requests.get(url).status_code == 200:
      return True
  except:
    return False 

def check_url ():
  while True: 
    input_url = input("Welcome to IsItDown.py!\nPlease write URL or URLS you want to check. (Separated by comma)\n").split(",")
    for url in input_url:
      url = url.strip().lower()
      if "." in url:
        if "http" in url:
          pass
        else:
          url = "http://" + url
        if is_legit(url):
          print(url,"is up!")
        else: 
          print(url,"is down!")
      else: 
        print(url, "is not a valid url")
    ask_exit()
  
def ask_exit():
    while True:
      ask = input("Do you want to start over? y/n \n"
      ) 
      if ask == 'y':
        os.system("clear")
        break
      elif ask == 'n':
        print("k, bye")
        sleep(2)
        os.system("clear")
        return False
      else:
        print("That's not a valid answer")
        continue
      
check_url()

