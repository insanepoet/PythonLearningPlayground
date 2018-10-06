import requests

'''
  Toying with Requests
'''

params = {"?q": "Pizza"}

r = requests.get("http://bing.com/search", params=params) # get with extra parameters

print(r.url) # print requested url
print("Status:", r.status_code) # Print Status
contents =  r.text

f = open("./page.html", "w+") # generate local html for testing
f.write(contents) # put requested html into the new file

'''
  Toying with Posts
'''

my_data = {"name": "Bob", "email": "Bob@dole.com"}

r = requests.post("http://w3schools.com/php/welcome.php") # post my_data

f=open("myfile.html", "w+")
f.write(r.text)