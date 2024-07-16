# You can use the datetime module to handle dates
# it's a good idea to just import the class
from datetime import datetime

# you can use today to get the current date
now = datetime.today()

print(now)

# and you can access it's attributes
print(now.year)

# or you can create custom dates
birthday = datetime(year=1996, month=3, day=16)

print(birthday)
