from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):
    # ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        # assert that the response code of 'incidents/escalators returns a 200 code
        self.assertEqual(escalator_response, 200, "Expected HTTP 200 for /incidents/escalators")

        elevator_response = app.test_client().get('/incidents/elevators').status_code
        # assert that the response code of 'incidents/elevators returns a 200 code
        self.assertEqual(escalator_response, 200, "Expected HTTP 200 for /incidents/escalators")
################################################################################

    # ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response assert that each of the required fields
        # are present in the response
        for incident in json_response:
            for field in required_fields:
                self.assertIn(field, incident, f"Missing required field '{field}' in incident")

################################################################################

    # ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"
        for incident in json_response:
            self.assertEqual(incident.get("UnitType"), "ESCALATOR", "Expected UnitType 'ESCALATOR'")

################################################################################

    # ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        for incident in json_response:
            self.assertEqual(incident.get("UnitType"), "ELEVATOR", "Expected UnitType 'ELEVATOR'")

################################################################################

if __name__ == "__main__":
    unittest.main()