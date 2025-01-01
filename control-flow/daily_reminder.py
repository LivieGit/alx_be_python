def create_daily_reminder():
  """
  This function prompts the user for a task, its priority, time sensitivity, 
  and allows for customized reminders, returning a reminder message accordingly.
  """
  task = input("Enter your task: ")

  # Check for customized reminder message
  custom_reminder = input("Do you want to enter a custom reminder message? (yes/no): ").lower()
  if custom_reminder == "yes":
      reminder_message = input("Enter your custom reminder message: ")
  else:
      priority = input("Priority (high/medium/low): ").lower()
      time_bound = input("Is it time-bound? (yes/no): ").lower()

      # Process task based on priority and time sensitivity (if no custom message)
      match priority:
          case "high":
              message = f"Reminder: '{task}' is a high priority task"
          case "medium":
              message = f"Reminder: '{task}' is a medium priority task"
          case "low":
              message = f"Note: '{task}' is a low priority task"

      # Add urgency if the task is time-bound
      if time_bound == "yes":
          message += " that requires immediate attention today!"

      reminder_message = message

  return reminder_message

# Get and print the reminder message
reminder_message = create_daily_reminder()
print(reminder_message)
