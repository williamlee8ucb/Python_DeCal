# INTRODUCTION TO DICTIONARIES

# Examples
# {key : value, key : value, etc.}
# value can be any data type

fourth_planet = {
    "name" : "Mars", 
    "moons" : ["Phobos", "Deimos"], 
    "diameter_km" : 6337, 
    "atmosphere" : False
}

print(fourth_planet)

# print specific values of a key
print(fourth_planet["name"])
print(fourth_planet.get("moons"))

# Modify a dictionary
fourth_planet["atmosphere"] = True
print(fourth_planet.get("atmosphere"))

# Add a new section of a dictionary
fourth_planet["color"] = "Red"
print(fourth_planet)

# Remove items from a dictionary
fourth_planet.pop("name")
print(fourth_planet)

del fourth_planet["moons"]
print(fourth_planet)
