# TaskTimer

`TaskTimer` is a Python class used to schedule and keep track of upcoming actions. You can use `TaskTimer` to automatically calculate and execute when a given function will be executed based on a specified duration in seconds.

# Usage
To use the TaskTimer class, you need to initialize an instance of the class with an action name, function and the amount of seconds until the function will be executed.

    from task_timer_birdhouses import TaskTimer

#### Initialize a new TaskTimer
    def greet(name):
        print(f"Hello, {name}!")

    task_timer = TaskTimer('greeting', 5, greet, args=["John"])

#### Print the next action time in a human-friendly format
    print(task_timer.human_friendly())

    # Output
    June 21, 2023, 02:11 AM

#### Print the next action time as a datetime object
    print(str(task_timer))

    # Output
    2023-06-21 02:11:05.046499

#### Print all upcoming actions
    print(TaskTimer.get_upcoming_actions())

    # Output
    {'send_email': 'June 21, 2023, 02:11 AM'}

In the example above, 'send_email' is the action we're scheduling, and 3600 is the number of seconds until the action will be executed.

### Other use cases
If you just want to add the sleep time in seconds to the current time you can do this:

        task_timer = TaskTimer('test', 5)

        print(task_timer)
        # Output
        2023-06-21 13:03:53.582599

        print(task_timer.human_friendly())
        # Output
        June 21, 2023, 02:11 AM

This might be useful if you use a different setup for executing your functions, and you only want to display the time a function will be executed.
## Installation

This package can be installed using pip:

```bash
pip install task-timer-birdhouses
