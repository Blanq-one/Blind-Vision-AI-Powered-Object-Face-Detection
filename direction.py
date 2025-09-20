import urllib.parse
import json
import pyttsx3
import requests
import tensorflow as tf
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Retrieve location details based on IP address
response = requests.get("http://ip-api.com/json/").json()

# Extract latitude and longitude from the response
latitude = response['lat']
longitude = response['lon']

print("Your current location:")
print("Latitude:", latitude)
print("Longitude:", longitude)

# Your Bing Maps Key 
bingMapsKey = "ApFr1grOeMUw9DEV4sPm60bcgz1Ye6flK6FHfPqN97tDp0BsJVsf9uQxA1Myo2AF"

# Function to get destination from user's speech input
def get_destination():
    with sr.Microphone() as source:
        print("Please say the destination:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        destination = recognizer.recognize_google(audio)
        print("Destination:", destination)
        return destination
    except sr.UnknownValueError:
        print("Sorry, could not understand the destination.")
        return None
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))
        return None

# Get destination from user
destination = get_destination()
if destination:
    # Encode destination for URL
    encodedDest = urllib.parse.quote(destination, safe='')

    # Construct the route URL
    routeUrl = f"http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0={latitude},{longitude}&wp.1={encodedDest}&key={bingMapsKey}"

    # Retrieve route information
    response = requests.get(routeUrl)
    result = response.json()

    # Extract driving directions from the route information
    itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]

    # Read out the driving directions
    for item in itineraryItems:
        instruction_text = item["instruction"]["text"]
        print(instruction_text)  # Print directions to console
        engine.say(instruction_text)  # Speak directions
        engine.runAndWait()
