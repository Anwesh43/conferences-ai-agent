from services.base_http_client import BaseHTTPClient
import os 
from dotenv import load_dotenv 
from services.common_response import handleError 

load_dotenv()

class ConferenceService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["CONFERENCE_BASE_URL"])
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:157.0) Gecko/20100101 Firefox/157.0"
        }

    def getConferences(self):
        try:
            response = self.client.getCall("conferences", qpParams={}, headers = self.headers)
            if "hits" in response:
                if "hits" in response["hits"]:
                    hits = response["hits"]["hits"]
                    result = []
                    for hit in hits:
                        obj = {}
                        obj["id"] = hit["id"]
                        if "metadata" in hit and "addresses" in hit["metadata"] and len(hit["metadata"]["addresses"]) > 0:
                            obj["address"] = hit["metadata"]["addresses"][0]
                        if "titles" in hit and len(hit["titles"]) > 0 and "title" in hit["titles"][0]:
                            obj["title"] = hit["titles"][0]["title"]
                        result.append(obj)
                    return result 
        except Exception as e:
            return handleError(e)

    def getConference(self, id : str):
        try: 
            response = self.client.getCall(f"conferences/{id}", qpParams={}, headers=self.headers)
            return response 
        except Exception as e:
            return handleError(e)
    
