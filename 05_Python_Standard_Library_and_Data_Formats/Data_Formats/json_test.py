import json

user_profile = {
    "name" : "Suresh",
    "age" : 26,
    "is_active" : True,
    "skills" : ["Python", "JavaScript", "SQL"]
}

# create a json file and write data to it
with open("user_profile.json", "w") as file:
    json.dump(user_profile, file, indent=4)
print("JSON file saved successfully.")

# read json file and print data
with open("user_profile.json", "r") as file:
    loaded_data = json.load(file)

    print("name:", loaded_data["name"])
    print("skills:", loaded_data["skills"])