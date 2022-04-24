# https://leetcode.com/problems/design-underground-system/


class UndergroundSystem:

    def __init__(self):
        self.customer_check_in = {}  # id: (station, t)
        self.station_to_station = {}  # (station1, station2): [t, counter]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_check_in, time = self.customer_check_in.pop(id)
        ride = (station_check_in, stationName)
        td = t - time
        if ride in self.station_to_station:
            self.station_to_station[ride][0] += td
            self.station_to_station[ride][1] += 1
        else:
            self.station_to_station[ride] = [td, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, counter = self.station_to_station[(startStation, endStation)]
        return time / counter
