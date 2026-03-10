d = {"name": "Sai", "age": 20}

# Access
print(d["name"])

# Update
d["age"] = 21

# Add
d["city"] = "Mumbai"

# Remove
d.pop("age")

# Merge
d2 = {"course": "BCA"}
d.update(d2)

print(d)