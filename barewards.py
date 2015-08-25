import requests
import datetime

class BARewards:
    base_uri = "http://dev1-flightavail-avios.bitnamiapp.com:8080/flight-availability-ws/departure/cities/{frm}/destination/{to}?obDate={today}&cabinClass={klass}&sc={sc}"

    cabins = {
        "economy": "X",
        "premium": "P",
        "business": "U",
        "first": "Z",
    }

    def availability(self, frm, to, klass="economy", number_of_seats=1):
        if klass not in self.cabins:
            raise "You must specify a valid fare class."

        sc = self.cabins[klass]
        klass = klass.upper()

        today = datetime.date.today().strftime("%d%m%Y")

        response = requests.get(self.base_uri.format(frm=frm, to=to, today=today, klass=klass, sc=sc))

        if response.status_code != 200:
            raise "The server responded with an error."

        json = response.json()

        avios_price = None
        if "prices" in json and "prices" in json['prices'] and "A" in json['prices']['prices']:
            avios_price = json['prices']['prices']['A']

        return {
            "city": json['cityName'],
            "country": json['countryName'],
            "region": json['regionName'],
            "reward_flight_saver": "prices" in json and "rfs" in json['prices'] and json['prices']['rfs'],
            "availability_dates": self.parse_availability_dates(json, number_of_seats),
            "avios_price": avios_price,
            "raw_response": json,
        }
        
    def parse_availability_dates(self, json, number_of_seats):
        available = [entry for entry in json['out'] if entry['bs'] >= number_of_seats]
        #TODO parse the dates
        return available
