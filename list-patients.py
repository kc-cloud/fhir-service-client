import requests
import json

url = "https://ws4healthdataservice-cf-patients-fhir-service.fhir.azurehealthcareapis.com/Patient"

payload = ""
headers = {
  'Authorization': 'Bearer ',
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
