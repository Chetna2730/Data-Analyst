from datetime import datetime

def diff_date(date1, date2):
    # Convert tuples to datetime objects
    date1 = datetime(*date1)
    date2 = datetime(*date2)

    # Calculate the difference between the two dates
    delta = abs(date2 - date1)

    # Return the number of days
    return delta.days

# Sample dates
date1 = (2014, 7, 2)
date2 = (2014, 7, 11)

# Calculate the number of days between the dates
days = diff_date(date1, date2)
print("Number of days between {} and {}: {}".format(date1, date2, days))
#--------------------------------------
