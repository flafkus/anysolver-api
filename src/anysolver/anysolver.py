from typing import Optional

import requests

API_BASE = "https://api.anysolver.com"
DEFAULT_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36'

class AnySolver():
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        
        
    ### example task:
    
    def createTask(self, task: dict, settings: Optional[dict] = None) -> str:
        data = {
            "clientKey": self.API_KEY,
            "task": task
        }

        if settings:
            data["settings"] = settings
            
        res = requests.post(f"{API_BASE}/createTask", json=data).json()
        if res["errorId"] != 0:
            # error here
            print("some catch here")
        
        return res
        
        