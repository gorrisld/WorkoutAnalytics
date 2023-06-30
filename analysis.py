import pandas as pd
import matplotlib.pyplot as plt

class Analyze():
    def analyzeWalking(workouts):
        # Filter workouts with workout_activity_type of HKWorkoutActivityTypeWalking
        walking_workouts = [workout for workout in workouts if workout.workout_activity_type == "HKWorkoutActivityTypeRunning"]

        # Create lists to store the data
        dates = []
        distances = []
        durations = []
        energies = []

        # Iterate over the walking workouts
        for workout in walking_workouts:
            # Extract relevant information
            start_date = pd.to_datetime(workout.start_date)
            distance_statistic = next((statistic for statistic in workout.workout_statistics if statistic[0] == "HKQuantityTypeIdentifierDistanceWalkingRunning"), None)
            energy_statistic = next((statistic for statistic in workout.workout_statistics if statistic[0] == "HKQuantityTypeIdentifierActiveEnergyBurned"), None)

            # Append data to lists
            dates.append(start_date)
            distances.append(float(distance_statistic[3]) if distance_statistic else None)
            durations.append(float(workout.duration) if workout.duration else None)
            energies.append(float(energy_statistic[3]) if energy_statistic else None)

        # Create a DataFrame with the collected data
        data = pd.DataFrame({
            "Date": dates,
            "Distance": distances,
            "Duration": durations,
            "Energy": energies
        })

        # Plot the progression of distance and energy over time
        fig, ax = plt.subplots()
        ax.plot(data["Date"], data["Distance"], label="Distance")
        ax.plot(data["Date"], data["Energy"], label="Energy")
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")
        ax.set_title("Progression of Distance and Energy over Time")
        ax.legend()

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)

        # Display the plot
        plt.show()

    def analyzeRunning(workouts):
        # Filter workouts with workout_activity_type of HKWorkoutActivityTypeRunning
        running_workouts = [workout for workout in workouts if workout.workout_activity_type == "HKWorkoutActivityTypeRunning"]

        # Create lists to store the data
        dates = []
        distances = []
        durations = []
        energies = []

        # Iterate over the running workouts
        for workout in running_workouts:
            # Extract relevant information
            start_date = pd.to_datetime(workout.start_date)
            distance_statistic = next((statistic for statistic in workout.workout_statistics if statistic[0] == "HKQuantityTypeIdentifierDistanceWalkingRunning"), None)
            energy_statistic = next((statistic for statistic in workout.workout_statistics if statistic[0] == "HKQuantityTypeIdentifierActiveEnergyBurned"), None)

            # Append data to lists
            dates.append(start_date)
            distances.append(float(distance_statistic[3]) if distance_statistic else None)
            durations.append(float(workout.duration) if workout.duration else None)
            energies.append(float(energy_statistic[3]) if energy_statistic else None)

        # Create a DataFrame with the collected data
        data = pd.DataFrame({
            "Date": dates,
            "Distance": distances,
            "Duration": durations,
            "Energy": energies
        })

        # Plot the progression of distance and energy over time
        fig, ax = plt.subplots()
        ax.plot(data["Date"], data["Distance"], label="Distance")
        ax.plot(data["Date"], data["Energy"], label="Energy")
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")
        ax.set_title("Progression of Distance and Energy over Time")
        ax.legend()

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)

        # Display the plot
        plt.show()

    def SuggestWorkout():
        print("Workout")