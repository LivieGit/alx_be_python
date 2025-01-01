def create_daily_reminder():
  """
  This function prompts the user for a task, its priority, and time sensitivity,
  and returns a reminder message accordingly.
  """
  # Get user input for the task
  task = input("Enter your task: ")

  # Get user input for priority
  priority = input("Priority (high/medium/low): ").lower()

  # Get user input for time sensitivity
  time_bound = input("Is it time-bound? (yes/no): ").lower()

  # Process task based on priority and time sensitivity
  reminder_message = match priority:
      case "high":
          message = f"Reminder: '{task}' is a high priority task"
      case "medium":
          message = f"Reminder: '{task}' is a medium priority task"
      case "low":
          message = f"Note: '{task}' is a low priority task"

  # Add urgency if the task is time-bound
  if time_bound == "yes":
      message += " that requires immediate attention today!"

  return message  # Return the reminder message

# Print an example reminder message
reminder_message = create_daily_reminder()
print(reminder_message)
