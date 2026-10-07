from tools.conf_tools import getPhotosForLocation, getConferenceDetails, getConferences, searchForNearestItem
from typing import Dict 
import json 

def writeFile(fileName : str, data : Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data to {fileName}")


if __name__ == "__main__":
    conferences = getConferences()
    writeFile("conf.json", conferences)
    conference1Id = conferences[0]["id"]
    latitude = conferences[0]["address"]["latitude"]
    longitude = conferences[0]["address"]["longitude"]
    writeFile("test_conf1.json", getConferenceDetails(conference1Id))
    locations = searchForNearestItem("pizza", latitude=str(latitude), longitude=str(longitude))
    writeFile("test_places.json", locations)
    dataId = locations[0]["data_id"]
    writeFile("test_place_pics.json", getPhotosForLocation(dataId=dataId))