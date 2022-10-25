import requests
import json

class Model:
    def __init__(self):
        self.message_url = "https://tie.digitraffic.fi/api/traffic-message/v1/messages"
        self.message_data = []

    def get_message_data(self, type):
        params = {
            "situationType": type,
            "inactiveHours": 0,
            "includeAreaGeometry": False
            }
        res = requests.get(url=self.message_url, params=params)
        data = json.loads(res.text)

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
