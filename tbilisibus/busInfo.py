class BusInfo:
    def __init__(self, route="", text="", time=""):
        self.route = route
        self.text = text
        self.time = time

    def __str__(self):
        return self.route + " | " + self.text + " --  " + self.time + " min."

    def __repr__(self):
        return self.__str__()
