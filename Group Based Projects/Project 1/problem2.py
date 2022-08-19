# Group Exercises 1

# Teammates: Luke Zerrer, Lance Wong

# Problem 2 - 24-hour Clock

# A day has 86,400 secs (24 * 60 * 60). Given a
#  number in the range 1 to 86,400 (inclusive),
#  output the corresponding time
#  as hours, minutes and seconds in
#  a 24-hour clock format. 
# For example 70,000 seconds
#  is "19 hours, 26 minutes, and 40 seconds". Your
#  program should ask the user to type in a number
#  of seconds and then print the time. Make
#  sure you correctly format the case where
#  one or more of the values is 1, for
#  example "1 hour, 1 minute, and 1 second".



# make function to check if the unit should be singular or plural
# if name should be plural it adds an "s" to it
def plurilized(quantity, unit):
  plural = "{} {}s"
  singular = "{} {}"
  if quantity != 1:
    result = plural.format(quantity, unit)
  else:
    result = singular.format(quantity, unit)
  return result
    
#input seconds
total_seconds = int(input("Please input the number of seconds: "))
original_seconds = total_seconds
# number of hours
number_hours = total_seconds // 3600
total_seconds = total_seconds - number_hours * 3600
# number of minutes
number_minutes = total_seconds // 60
total_seconds = total_seconds - number_minutes * 60
# number of seconds
number_seconds = total_seconds

# uses the quantity found for each unit of the user's input
# and uses the pluralized funtion to determin proper grammar
# it produces a grammatically correct string
result = "{} is {} {} {}".format(
  original_seconds,
  plurilized(number_hours, "hour"),
  plurilized(number_minutes, "minute"),
  plurilized(number_seconds, "second")
)


print(result)
