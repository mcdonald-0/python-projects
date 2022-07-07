def seconds_in_a_day():
    seconds = 60
    minutes = seconds * 60
    hours = minutes * 24
    return hours

def seconds_in_a_given_number_of_days(number_of_days):
    global seconds_in_a_day
    number_of_days = int(number_of_days)
    days_to_seconds = seconds_in_a_day() * number_of_days
    return days_to_seconds

def seconds_in_a_week():
    global seconds_in_a_day
    week_to_seconds = seconds_in_a_day() * 7
    return week_to_seconds

def seconds_in_a_given_number_of_weeks(number_of_weeks):
    global seconds_in_a_week
    number_of_weeks = int(number_of_weeks)
    weeks_to_seconds = seconds_in_a_week() * number_of_weeks
    return weeks_to_seconds

def seconds_in_a_month(number_of_days):
    global seconds_in_a_day
    number_of_days = int(number_of_days)
    month_to_seconds = seconds_in_a_day * number_of_days
    return month_to_seconds

def seconds_in_a_year():
    global seconds_in_a_day
    year_to_seconds = seconds_in_a_day() * 365.25
    return year_to_seconds

def seconds_in_a_given_number_of_years(number_of_years):
    global seconds_in_a_year
    number_of_years = int(number_of_years)
    years_to_seconds = seconds_in_a_year() * number_of_years
    return years_to_seconds





# -------------------------------- NOTE --------------------------------- #
'''
This is a list of functions dependent on each other that helps to convert days, months and years to seconds.
It may come in handy...!
--- 09:30, 07-07-2022 ---
'''
