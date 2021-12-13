seconds = int(input("Enter number of seconds: "))

hours = seconds // 3600
seconds_remain = seconds % 3600

minutes = seconds_remain // 60
actual_seconds = seconds_remain % 60

print(str(seconds), " seconds is ", str(hours)," hours, ",str(minutes)," minutes, and ", str(actual_seconds), " seconds")