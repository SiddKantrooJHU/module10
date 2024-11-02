import json
import requests
from flask import Flask

# API endpoint URL's and access keys
# WMATA_API_KEY = "47ba80d835004e3985d5559e24e99bcc"
INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"
headers = {'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
  # create an empty list called 'incidents'
  incidents = []   
  # use 'requests' to do a GET request to the WMATA Incidents API
  # retrieve the JSON from the response
  response = requests.request("GET", INCIDENTS_URL, headers=headers)
  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
  #   -StationCode, StationName, UnitType, UnitName
  # add each incident dictionary object to the 'incidents' list
  if response.status_code == 200:
    data= response.json()
    for incident in data.get("ElevatorIncidents", []):
      if incident['UnitType'].lower() == unit_type.lower():
        incidents.append({
          'StationCode': incident['StationCode'],
          'StationName': incident['StationName'],
          'UnitType': incident['UnitType'],
          'UnitName': incident['UnitName']
        })
  # return the list of incident dictionaries using json.dumps()
  return json.dumps(incidents)

if __name__ == '__main__':
    app.run(debug=True)
