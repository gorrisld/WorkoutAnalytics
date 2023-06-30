import xml.etree.ElementTree as ET
from datetime import datetime
from workout import Workout

class UserProfile:
    def __init__(self, name, password, heightIn, heightFt):
        self.name = name
        self._password = password
        self.height_in = heightIn
        self.height_ft = heightFt
        self.workouts = []
        self.goals = []

    def addGoal(self, goal):
        self.goals.append(goal)

    def deleteGoal(self, goal):
        if goal in self.goals:
            self.goals.remove(goal)
        else:
            print("Goal not found.")

    def addGoal(self, distance, timeGoal, completionDate):
        goal = {
            'distance': distance,
            'timeGoal': timeGoal,
            'completionDate': completionDate
        }
        self.goals.append(goal)

    def deleteWorkout(self, workout):
        if workout in self.workouts:
            self.workouts.remove(workout)
        else:
            print("Workout not found.")

    def importData(self, fileName):
        # Code to import data and update the profile
        tree = ET.parse(fileName)
        root = tree.getroot()
        workouts = []
        workout_elements = root.findall('.//Workout')
        if workout_elements:
            # Iterate over the found elements
            for element in workout_elements:
                # Remove the WorkoutRoute element
                workout_route = element.find('WorkoutRoute')
                if workout_route is not None:
                    element.remove(workout_route)

                # Create a Workout object with the modified element
                workout = Workout(element)

                # Append the workout object to the list
                workouts.append(workout)

        else:
            print("No Workout elements found in the XML document.")

        # Access the workout objects and their attributes as needed
        for workout in workouts:
            print(workout.workout_activity_type)
            print(workout.duration)
            # Access other attributes of the workout object as needed
            print("------------------")

        self.workouts = workouts
        
    def exportData(self):
        # Code to export the profile data
        # Create the root element for the XML document
        root = ET.Element("Workouts")

        # Iterate over the list of Workout objects
        for workout in self.workouts:
            # Create the Workout element
            workout_element = ET.SubElement(root, "Workout")
            workout_element.set("workoutActivityType", workout.workout_activity_type)
            workout_element.set("duration", workout.duration)
            workout_element.set("durationUnit", workout.duration_unit)
            workout_element.set("sourceName", workout.source_name)
            workout_element.set("sourceVersion", workout.source_version)
            workout_element.set("device", workout.device)
            workout_element.set("creationDate", workout.creation_date)
            workout_element.set("startDate", workout.start_date)
            workout_element.set("endDate", workout.end_date)

            # Add MetadataEntry elements
            for key, value in workout.metadata_entries:
                metadata_entry = ET.SubElement(workout_element, "MetadataEntry")
                metadata_entry.set("key", key)
                metadata_entry.set("value", value)

            # Add WorkoutEvent elements
            for event_type, date, duration, duration_unit in workout.workout_events:
                workout_event = ET.SubElement(workout_element, "WorkoutEvent")
                workout_event.set("type", event_type)
                workout_event.set("date", date)
                workout_event.set("duration", duration)
                workout_event.set("durationUnit", duration_unit)

            # Add WorkoutStatistics elements
            for statistic_type, start_date, end_date, sum_value, unit in workout.workout_statistics:
                workout_statistic = ET.SubElement(workout_element, "WorkoutStatistics")
                workout_statistic.set("type", statistic_type)
                workout_statistic.set("startDate", start_date)
                workout_statistic.set("endDate", end_date)
                workout_statistic.set("sum", sum_value)
                workout_statistic.set("unit", unit)

        # Create the XML tree
        tree = ET.ElementTree(root)

        # Save the XML to a file
        tree.write("workouts.xml", encoding="utf-8", xml_declaration=True)

        
    def editProfile(self, newName, newPassword, newHeightIn, newHeightFt):
        self.name = newName
        self._password = newPassword
        self.height_in = newHeightIn
        self.height_ft = newHeightFt