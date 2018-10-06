import simplejson as json # outside library renamed as json
import os

# Creating a new file (tmp until written)
newfile =open("newfile.txt", "w+")

# some basic content to write
string = "This will be the content of the txt file."

# write the string to the file and create it
newfile.write(string)

'''
transform json to an object for read / write

r+ - read and write
w+ - write

'''

if os.path.isfile("./ages.json") and  os.stat("./ages.json").st_size != 0: # check if file exists and size is > 0
    old_file = open("./ages.json", "r+") # load the file into python
    data = json.loads(old_file.read()) # set the data into an object
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Nick", "age": 27}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
