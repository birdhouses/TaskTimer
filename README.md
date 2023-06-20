# TaskTimer

`TaskTimer` is a Python class used to schedule and keep track of upcoming actions. You can use `TaskTimer` to automatically calculate when a given action will be executed based on a specified duration in seconds.

# Usage
To use the TaskTimer class, you need to initialize an instance of the class with an action and the amount of seconds until the action will be executed.

    from task_timer import TaskTimer

# Initialize a new ActionScheduler
    task_timer = TaskTimer('send_email', 3600)

# Print the next action time in a human-friendly format
    print(task_timer.human_friendly())

# Print the next action time as a datetime object
    print(str(task_timer))

# Print all upcoming actions
    print(TaskTimer.get_upcoming_actions())

In the example above, 'send_email' is the action we're scheduling, and 3600 is the number of seconds until the action will be executed.


## Installation

This package can be installed using pip:

```bash
pip install task-timer
