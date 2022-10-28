import requests
import json

class Model:
    def __init__(self):
        self.tasks_data = {}
        self.conditions_data = {}
        self.message_data = []

    def get_tasks_data(self, input):
        url = "https://tie.digitraffic.fi/api/maintenance/v1/tracking/tasks"
        params = {}
        res = requests.get(url=url, params=params)
        data = json.loads(res.text)

        # TODO: parse the road maintenance data
        self.tasks_data = data[0]

        return self.tasks_data

    def get_conditions_data(self, input):
        url = "https://tie.digitraffic.fi/api/v3/data/road-conditions"
        params = "/21/61/22/62"
        url += params
        res = requests.get(url=url)
        data = json.loads(res.text)

        # TODO: parse the road conditions data
        self.conditions_data = data["weatherData"][0]["roadConditions"][0]

        return self.conditions_data

    def get_messages_data(self, type):
        url = "https://tie.digitraffic.fi/api/traffic-message/v1/messages"
        params = {
            "situationType": type,
            "inactiveHours": 0,
            "includeAreaGeometry": False
            }
        res = requests.get(url=url, params=params)
        data = json.loads(res.text)

        # parse the traffic messages data
        self.message_data = []
        for feature in data['features']:
            row = {}
            try:
                row['countryCode'] = feature['properties']['announcements'][0]['location']['countryCode']
            except:
                row['countryCode'] = None
            try:
                row['municipality'] = feature['properties']['announcements'][0]['locationDetails']['roadAddressLocation']['primaryPoint']['municipality']
            except:
                row['municipality'] = None
            try:
                row['road'] = feature['properties']['announcements'][0]['locationDetails']['roadAddressLocation']['primaryPoint']['roadAddress']['road']
            except:
                row['road'] = None
            try:
                row['description'] = feature['properties']['announcements'][0]['location']['description']
            except:
                row['description'] = None
            self.message_data.append(row)

        return self.message_data
