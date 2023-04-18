class FlightData:

    def __init__(self, data):
        self.price = data['conversion']['PLN']
        self.dep_city = data['cityFrom']
        self.dep_iata = data['flyFrom']
        self.dst_city = data['cityTo']
        self.dst_iata = data['flyTo']
        flies = data['route']
        out_b = flies[0]['local_arrival']
        in_b = flies[1]['local_departure']
        self.outbound = out_b.split("T")[0]
        self.inbound = in_b.split("T")[0]
