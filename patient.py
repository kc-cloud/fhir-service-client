import requests
import json

url = "https://ws4healthdataservice-cf-patients-fhir-service.fhir.azurehealthcareapis.com/Patient"

payload = json.dumps({
  "resourceType": "Patient",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Ganesan Sivan</div>"
  },
  "extension": [
    {
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
      "valueCodeableConcept": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/v3/Race",
            "code": "2029-7",
            "display": "Asian Indian"
          }
        ],
        "text": "race"
      }
    },
    {
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
      "valueCodeableConcept": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/v3/Ethnicity",
            "code": "2186-5",
            "display": "Nonhispanic"
          }
        ],
        "text": "ethnicity"
      }
    },
    {
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
      "valueCode": "M"
    }
  ],
  "identifier": [
    {
      "system": "http://va.gov/fhir/NamingSystem/identifier",
      "value": "VA-101"
    },
    {
      "system": "http://fhirbot.org",
      "value": "555122"
    }
  ],
  "name": [
    {
      "use": "official",
      "text": "Ganesan Sivan",
      "family": "Sivan",
      "given": [
        "Ganesan"
      ]
    }
  ],
  "telecom": [
    {
      "system": "phone",
      "value": "617-871-6778",
      "use": "mobile"
    },
    {
      "system": "email",
      "value": "Ganesan@busybee.com"
    }
  ],
  "gender": "male",
  "birthDate": "1990-10-07",
  "address": [
    {
      "use": "home",
      "line": [
        "150 Google Drive"
      ],
      "city": "Sharon",
      "state": "MA",
      "postalCode": "02067",
      "country": "USA"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer '
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

