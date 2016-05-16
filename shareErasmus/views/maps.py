import requests
import json

def getLatLngData(university_name, city):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + \
          university_name + "," + city + "&key=AIzaSyBJoL69cmn3X1Uf23j47Dzh-yeCnMACXf8"
    response = requests.get(url)
    response = response.json()
    lat = response['results'][0]['geometry']['location']['lat']
    lng = response['results'][0]['geometry']['location']['lng']
    latLng = {'lat': lat, 'lng': lng}

    return latLng