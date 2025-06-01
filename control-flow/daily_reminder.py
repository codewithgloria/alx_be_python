# daily_reminder.py

# Prompt user for task description
task = input("Enter your task: ").strip()

# Prompt for task priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match case to handle different priority levels
reminder = ""

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Check if the task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder += ". (Time sensitivity unknown)"

# Print the final reminder
print(f"Reminder: {reminder}")