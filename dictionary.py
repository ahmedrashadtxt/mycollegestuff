Days={"Monday": "Working day", "Tuesday": "Working day", "Wednesday": "Working day","Sunday":"Holiday","Saturday":"Holiday"}
print(Days)

#Update key "Saturday"
Days["Saturday"] = "Working day"
print(Days)

#Remove key Wednesday
Days.pop("Wednesday")
print(Days)

#Remove last inserted item
Days.popitem()
print(Days)

#delete key value Monday
del Days["Monday"]
print(Days)

#Insert an item to dict
Days["Friday"] = "Movie Night"
print(Days)

#Clear all items in dictionay
Days.clear()
print(Days)

#deletes the dictionary
del Days
print(Days)