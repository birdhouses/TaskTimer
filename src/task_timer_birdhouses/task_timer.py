import datetime

class TaskTimer:
    upcoming_actions = {}

    def __init__(self, action, sleep_time_in_seconds):
        self.action = action
        self.sleep_time_in_seconds = sleep_time_in_seconds
        self.next_action_time = datetime.datetime.now() + datetime.timedelta(seconds=sleep_time_in_seconds)

        # Append the action and its execution time to the list of upcoming actions
        TaskTimer.upcoming_actions[action] = self.next_action_time

    def __str__(self):
        return str(self.next_action_time)

    def human_friendly(self):
        return self.next_action_time.strftime("%B %d, %Y, %I:%M %p")

    @staticmethod
    def get_upcoming_actions():
        return {action: time.strftime("%B %d, %Y, %I:%M %p") for action, time in TaskTimer.upcoming_actions.items()}
