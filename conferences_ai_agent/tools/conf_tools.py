from services.conference_service import ConferenceService 
from services.location_service import LocationService 

locationService = LocationService()
confService = ConferenceService()

def getConferences():
    print(f"Calling getConferences tool")
    return confService.getConferences()

def getConferenceDetails(conferenceId : str):
    print(f"Calling getConferenceDetails tool for {conferenceId}")
    return confService.getConference(id = conferenceId)

def searchForNearestItem(item : str, latitude : str, longitude: str):
    print(f"Calling searchForNearestItem tool {item} at {latitude}, {longitude}")
    return locationService.searchForNearestItem(item=item, latitude=latitude, longitude=longitude)

def getPhotosForLocation(dataId : str):
    print(f"Calling getPhotosForLocation tool for {dataId}")
    return locationService.getPhotosForLocation(dataId=dataId)

def writeHTML(htmlStr : str, fileName : str):
    print(f"Calling writeHTML tool for {fileName}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": 'success', 
        "message": f"Written html to {fileName}"
    }