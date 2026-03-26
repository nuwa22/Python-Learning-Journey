import datetime

# we use datetime module to work with date and time in Python
# now() method returns the current date and time as a datetime object
now = datetime.datetime.now()
print("Current date and time:", now)

# strftime() method formats the date and time as a string
formated_data = now.strftime("%Y-%m-%d")
print("Formated date:", formated_data)

# timedelta() method returns a timedelta object representing the difference between
# two datetime objects
tomorrow = now + datetime.timedelta(days=1)
print("Tomorrow's date:", tomorrow.strftime("%Y-%m-%d"))

