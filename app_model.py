import requests
import json
from urllib.parse import quote

class Model:
    """
    Model class of the MVC design pattern.

    This class gets all the data from the Digitraffic API and parses it to send
    it to the Controller.

    Attributes
    ----------
    tasks_per_day: dict
        The dict of road maintainance data as a histogram of tasks per day.
    conditions_data: dict
        The dict of road conditions data.
    messages_data: list
        The list of dicts of trafic messages data.
    coordinates: dict
        The dict of tuples of hardcoded locations.

    Methods
    -------
    get_tasks_data(inputs)
        Gets the road maintainance data from the API and parses it according to
        the user inputs.
    get_conditions_data(inputs)
        Gets the road conditions data from the API and parses it according to
        the user inputs.
    get_messages_data(type)
        Gets the traffic messages data from the API and parses it according to
        the user inputs.
    """

    def __init__(self):
        self.tasks_per_day = {}
        self.conditions_data = {}
        self.messages_data = []

        # hard coded co-ordinates: xMin, yMin, xMax, yMax
        self.coordinates = {
            "Helsinki": (24, 60, 26, 61),
            "Kuopio": (27, 62, 28, 64),
            "Oulu": (24, 64, 26, 66),
            "Pori": (21, 61, 22, 62),
            "Tampere": (23, 61, 24, 62),
        }


    def get_tasks_data(self, inputs):
        url = "https://tie.digitraffic.fi/api/maintenance/v1/tracking/routes"
        params = {
            # quote func to encode input text to URI format
            "endFrom": quote(inputs["end_time"]),
            "endBefore": quote(inputs["start_time"]),
            "xMin": self.coordinates[inputs["location"]][0],
            "yMin": self.coordinates[inputs["location"]][1],
            "xMax": self.coordinates[inputs["location"]][2],
            "yMax": self.coordinates[inputs["location"]][3],
            "domain": "state-roads",
            "taskId": "",
        }
        # join parameters with the api endpoint
        url += "?"
        url += "&".join(
            [f"{key}={params[key]}" for key in params.keys()]
        )

        res = requests.get(url=url)
        data = json.loads(res.text)

        # calculate tasks per day
        self.tasks_per_day = {}
        try:
            for feature in data['features']:
                for task in feature['properties']['tasks']:
                    self.tasks_per_day[task] = self.tasks_per_day.get(task,0)+1
        except:
            self.tasks_per_day = {}


    def get_conditions_data(self, inputs):
        url = "https://tie.digitraffic.fi/api/v3/data/road-conditions"

        # join input parameters with the api endpoint as queries
        url += "/" + "/".join(list(map(
            str, self.coordinates[inputs["location"]]
        )))
        res = requests.get(url=url)
        data = json.loads(res.text)

        # parse the conditions user inputs
        self.conditions_data = {}
        try:
            for item in data["weatherData"][0]["roadConditions"]:
                if item["forecastName"] == inputs["hour"].lower():
                    self.conditions_data = item
        except:
            self.conditions_data = {}


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
        self.messages_data = []
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
            self.messages_data.append(row)
