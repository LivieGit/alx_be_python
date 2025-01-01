# Daily reminder with priority and time sensitivity

# Get user input for the task
task = input("Enter your task: ")

# Get user input for priority
priority = input("Priority (high/medium/low): ").lower()

# Get user input for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority and time sensitivity
reminder_message = match priority:
    case "high":
        return f"Reminder: '{task}' is a high priority task"
    case "medium":
        return f"Reminder: '{task}' is a medium priority task"
    case "low":
        return f"Note: '{task}' is a low priority task"

# Add urgency if the task is time-bound
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"

# Print the reminder message
print(f"{reminder_message}")
