import requests

url = "https://login.microsoftonline.com/081a3ccb-0a61-4eaa-9bcc-386ad52326a3/oauth2/token"

payload = 'grant_type=client_credentials&client_id=11ca7773-f845-4bd8-a3bc-2e267b200e52&client_secret=y2j8Q~MN1Bjvzl9LRavTf8rpxb2J8p1ZxAUhgb88&resource=https%3A%2F%2Fws4healthdataservice-cf-patients-fhir-service.fhir.azurehealthcareapis.com'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'fpc=As3-IipBpHhPvb2PJ6loWFK73XlFAQAAAEwm9d0OAAAA'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
