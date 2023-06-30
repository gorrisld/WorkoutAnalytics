import time

# This class holds all the useful data from each workout
# class workout:

    # workoutType = ""
    # HRMin = 0
    # HRMax = 0 
    # HRAvg = 0
    # durationHour = 0
    # durationMin = 0
    # durationSec = 0.0
    # distance = 0.0
    # totalCals = 0
    # paceMin = 0
    # paceSec = 0
    # duration = time(0,0,0,0)

    # def __init(self):
    #     self.workoutType = ""

    # def workout(self, workoutType, HRMin, HRMax, HRAvg, durationHours, 
    #             durationMin, durationSec, distance, totalCals, paceMin, 
    #             paceSec):
    #     self.workoutType = workoutType
    #     self.HRMin = HRMin
    #     self.HRMax = HRMax
    #     self.HRAvg = HRAvg
    #     self.durationHour = durationHours
    #     self.durationMin = durationMin
    #     self.durationSec = durationSec
    #     self.distance = distance
    #     self.totalCals = totalCals
    #     self.paceMin = paceMin
    #     self.paceSec = paceSec

class Workout:
    def __init__(self, element):
        self.workout_activity_type = element.get('workoutActivityType')
        self.duration = element.get('duration')
        self.duration_unit = element.get('durationUnit')
        self.source_name = element.get('sourceName')
        self.source_version = element.get('sourceVersion')
        self.device = element.get('device')
        self.creation_date = element.get('creationDate')
        self.start_date = element.get('startDate')
        self.end_date = element.get('endDate')
        self.metadata_entries = self._extract_metadata_entries(element.findall('MetadataEntry'))
        self.workout_events = self._extract_workout_events(element.findall('WorkoutEvent'))
        self.workout_statistics = self._extract_workout_statistics(element.findall('WorkoutStatistics'))

    def _extract_metadata_entries(self, elements):
        metadata_entries = []
        for element in elements:
            key = element.get('key')
            value = element.get('value')
            metadata_entries.append((key, value))
        return metadata_entries

    def _extract_workout_events(self, elements):
        workout_events = []
        for element in elements:
            event_type = element.get('type')
            date = element.get('date')
            duration = element.get('duration')
            duration_unit = element.get('durationUnit')
            workout_events.append((event_type, date, duration, duration_unit))
        return workout_events

    def _extract_workout_statistics(self, elements):
        workout_statistics = []
        for element in elements:
            statistic_type = element.get('type')
            start_date = element.get('startDate')
            end_date = element.get('endDate')
            sum_value = element.get('sum')
            unit = element.get('unit')
            workout_statistics.append((statistic_type, start_date, end_date, sum_value, unit))
        return workout_statistics