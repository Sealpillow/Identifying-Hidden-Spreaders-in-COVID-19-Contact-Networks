class DailyNetworks:
    """
    A class to manage and compare networks on a daily basis.

    Methods:
        __init__():
            Initializes an empty dictionary to store networks by day.
        
        addNetworkByDay(day, newNetwork):
            Adds a network for a specific day.

        getNetworkByDay(day):
            Retrieves the network for a given day. Returns None if the day is not found.

    Attributes:
        networks (dict): A dictionary mapping days (keys) to their respective networks (values).
    """
    def __init__(self):
        self.networks = dict()
        self.totalConnections = 0

    def addNetworkByDay(self, day, newNetwork):
        self.networks[day] = newNetwork

    def getNetworkByDay(self, day):
        return self.networks.get(day)
    
    def calInfectionRate(self):
        # to find the day where the infection stops, susceptible number remains constant
        sCount = 0
        repeatedDays = 0
        prevCount = 0
        dayNum = 0
        for network in self.neworks.values():
            dayNum += 1
            for node in network.values(): # count the number of Susceptible individual per day
                if node.status=='A':
                    sCount +=1
            if sCount != prevCount:
                prevCount = sCount
                repeatedDays = 0
            else:
                repeatedDays +=1
            if repeatedDays > 2:
                return dayNum
        return dayNum


    
