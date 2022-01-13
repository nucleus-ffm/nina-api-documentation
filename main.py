import requests
import json

url_biwapp = 'https://warnung.bund.de/bbk.biwapp/warnmeldungen.json'
url_mowas = 'https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json'
url_katwarn = 'https://warnung.bund.de/bbk.katwarn/warnmeldungen.json'
url_dwd = 'https://warnung.bund.de/bbk.dwd/unwetter.json'
url_lhp = 'https://warnung.bund.de/bbk.lhp/hochwassermeldungen.json'

placesList = []
savedPlacesList = []

def loadJson(url):
    resp = requests.get(url=url)

    # check if request was sucessful
    if (resp.status_code == 200):
        print( url + " sucess")
        jsonData = json.loads(resp.text)
        # save all places in a list
        for alerts in jsonData:
            for places in alerts['info'][0]['area'][0]['geocode']:
                placesList.append(places['valueName'])
                #print(places["valueName"])


def loadAndSavedAllPlaces(placesList):
    # load already saved places 
    with open('listOfplaces.txt') as f:
        for line in f:
            #print(line)
            newElement = line[0:len(line)-1]
            savedPlacesList.append(newElement)

    print(savedPlacesList)
        

    # write all new places in the file
    with open('listOfplaces.txt', 'a') as f:
        for line in placesList:
            if line in savedPlacesList:
                print("already saved")
            else:
                f.write(line)
                f.write('\n')

def sortTextFile():
    savedPlacesList = []
    with open('listOfplaces.txt') as f:
        for line in f:
            #print(line)
            newElement = line[0:len(line)-1]
            savedPlacesList.append(newElement)
    
    savedPlacesList.sort()

    with open('listOfplaces.txt', 'r+') as f:
        for line in savedPlacesList:
            f.write(line)
            f.write('\n')

loadJson(url_biwapp)
loadJson(url_mowas)
loadJson(url_katwarn)
loadJson(url_dwd)
loadJson(url_lhp)

# remove dublicates in the list
placesList = list(dict.fromkeys(placesList))
loadAndSavedAllPlaces(placesList)
sortTextFile()