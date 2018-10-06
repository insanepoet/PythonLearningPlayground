import requests
from io import BytesIO
from PIL import Image

r = requests.get("http://walpapercave.com/wp/TuVhQdr.jpg")

print("status:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")