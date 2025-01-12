from datetime import datetime, timedelta

def display_current_datetime():
  """
  Prints the current date and time in YYYY-MM-DD HH:MM:SS format.
  """
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_date}")

def calculate_future_date(number_of_days):
  """
  Calculates and prints the future date after adding the specified number of days to the current date.

  Args:
      number_of_days: The number of days to add to the current date (integer).
  """
  current_date = datetime.now()
  future_date = current_date + timedelta(days=number_of_days)
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
  display_current_datetime()
  number_of_days = int(input("Enter the number of days to add to the current date: "))
  calculate_future_date(number_of_days)
