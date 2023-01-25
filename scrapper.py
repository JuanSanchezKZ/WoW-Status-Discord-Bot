import requests


getURL = "https://us.api.blizzard.com/data/wow/connected-realm/11?namespace=dynamic-us&locale=en_US&access_token=EUckrcx7tBQNK9eDm5IzuW95rpfOZMAudS"


def get_status():
  r = requests.get(url = getURL)
  data = r.json()

  status = data.get('status').get('name')


  if status == "Down":
        return "El servidor está caído"
  else:
        return "Ya se puede ingresar al servidor."
    
 

