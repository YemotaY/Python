# importing the requests library
import requests
  
# api-endpoint
URL = "http://localhost/index.php/user/list"
  
# location given here
rows = 1
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'limit':rows}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()

print(data)
print(r.text)
#f = open("RequestAnswer.txt","w")
#f.write(r.text)
#f.close()
  
  