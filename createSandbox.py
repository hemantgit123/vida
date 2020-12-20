import os
import time
os.system('pip3 install requests')
import requests
import json
import time
import random
# defining the api-endpoint for sandbox ceration
POST_API_ENDPOINT = "https://vida.esp-staging.vmware-aws.com/vida/api/v1/sandbox/"

# data to be sent to api 

data= {
"username" : "hemantg@vmware.com",
"cloudVendorId": 1,
"planId": 1

}
time.sleep(random.randint(5, 20))

jsonData = json.dumps(data)

headers = {"Content-Type": "application/json"} 

r = requests.post(url = POST_API_ENDPOINT, data = jsonData, headers=headers)

r_dictionary= r.json()

time.sleep(random.randint(5, 20))

GET_API_ENDPOINT = "https://vida.esp-staging.vmware-aws.com/vida/api/v1/sandbox/"+ "/"+ str (r_dictionary['id'])
r = requests.get(url = GET_API_ENDPOINT)

print ("===================Sandbox Created============\n")
json_data = json.loads(r.text)
print ("clivmExternalIP:",json_data['clivmExternalIP'])
print ("clivmExternalPort:",json_data['clivmExternalPort'])
print ("clivmPemFileURL:",json_data['clivmPemFileURL'])


sample_dict={}

sample_dict["clivmExternalIP"]=json_data['clivmExternalIP']
sample_dict["clivmExternalPort"]=json_data['clivmExternalPort']
sample_dict["clivmPemFileURL"]=json_data['clivmPemFileURL']

tkg_version=1.1
file_name="sandbox_"+str(tkg_version)+".json"

with open(file_name, "w") as write_file:
    json.dump(sample_dict, write_file)




