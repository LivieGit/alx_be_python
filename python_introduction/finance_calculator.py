# Personal finance calculator

# User input for income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual interest rate (assuming simple interest for simplicity)
interest_rate = 0.05  # 5%

# Calculate projected annual savings
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Print the results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings with {interest_rate*100}% interest are: ${projected_annual_savings:.2f}")
