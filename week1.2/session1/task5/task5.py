# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["river1"] = "on earth"
rivers["river2"] = "on mars"
print(rivers)

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.get("Leeds"))
print(rivers.get("London"))
print(rivers.get("Liverpool"))
print(rivers.get("river1"))
print(rivers.get("river2"))

# Display all the key:value pairs, as tuples
print(rivers.items())

# Delete an entry from the rivers database
rivers.pop("river2")
print(rivers)