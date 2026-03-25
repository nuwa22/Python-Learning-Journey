import json

movie = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "rating": 8.8
}

# create a json file and write data to it
with open("movie.json", "w") as file:
    json.dump(movie, file, indent=4)
print("JSON file saved successfully.")

# read json file and print data
with open("movie.json", "r") as file:
    loaded_movie = json.load(file)

    print("director:", loaded_movie["director"])