from typing import Optional
from anysolver.exceptions import AnySolverInternalError, AnySolverExternalError
from enum import Enum

import requests

API_BASE = "https://api.anysolver.com"

class AnySolver():
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        
    def createTask(self, task: dict, settings: Optional[dict] = None) -> str:
        data = {"clientKey": self.API_KEY, "task": task}
        if settings:
            data["settings"] = settings
        res = requests.post(f"{API_BASE}/createTask", json=data).json()
        
        if res['errorId'] == 1:
            raise AnySolverExternalError
        elif res['error'] == 2:
            raise AnySolverInternalError
        
        return res
    
    def getTaskResult(self, taskId: str) -> str:
        data = {"clientKey": self.API_KEY, "taskId": taskId}
        res = requests.post(f"{API_BASE}/getTaskResult", json=data).json()
        
        if res['errorId'] == 1:
            raise AnySolverExternalError
        elif res['error'] == 2:
            raise AnySolverInternalError
        
        return res

    def getBalance(self) -> str:
        data = {"clientKey": self.API_KEY}
        res = requests.post(f"{API_BASE}/getBalance", json=data).json()  
          
        if res['errorId'] == 1:
            raise AnySolverExternalError
        elif res['error'] == 2:
            raise AnySolverInternalError
        
        return res
    
    
    