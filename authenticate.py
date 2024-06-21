import requests

url = "https://login.microsoftonline.com/{{tenantId}}/oauth2/token"

payload = 'grant_type=client_credentials&client_id={{client-id}}&client_secret=<client-secret>&resource=https%3A%2F%2Fws4healthdataservice-test-patients-fhir-service.fhir.azurehealthcareapis.com'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
