from services.base_http_client import BaseHTTPClient
import os 
from dotenv import load_dotenv 
from services.common_response import handleError
load_dotenv()

class LocationService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["SERP_BASE_URL"])

    def searchForNearestItem(self, item : str, latitude: str, longitude: str):
        try:
            qpParams = {
                "q": item, 
                "ll": f"@{latitude},{longitude},14z",
                "engine": "google_maps",
                "api_key": os.environ["SERP_API_KEY"]
            }
            response = self.client.getCall("search", qpParams=qpParams)
            keys = ["title", "data_id", "gps_coordinates"]
            localResults =  response["local_results"]
            data = []
            for localResult in localResults:
                obj = {}
                for key in keys:
                    obj[key] = localResult[key]
                data.append(obj)
            return data 
        except Exception as e:
            return handleError(e)

    def getPhotosForLocation(self, dataId : str):
        try:
            qpParams = {
                "data_id": dataId,
                "engine": "google_maps_photos",
                "api_key": os.environ["SERP_API_KEY"]
            }
            response = self.client.getCall("search", qpParams=qpParams)
            return response["photos"]
        except Exception as e:
            return handleError(e)