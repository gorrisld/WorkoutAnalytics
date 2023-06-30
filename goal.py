class Goal:
    def __init__(self, exerciseType, objective, workouts, suggestions):
        self.exercise_type = exerciseType
        self.objective = objective
        self.workouts = workouts
        self.suggestions = suggestions
    
    def applyWorkout(self, workout):
        self.workouts.append(workout)
    
    def deleteWorkout(self, workout):
        if workout in self.workouts:
            self.workouts.remove(workout)
        
    def createGoal(self):
        print("Not sure what we need here")