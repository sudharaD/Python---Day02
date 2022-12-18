age = int(input("How old are you? "))

remaining_years = 90 - age
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

message = f"you have left {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left."

print(message)
