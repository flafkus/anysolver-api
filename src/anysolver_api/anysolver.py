import time

import requests

from anysolver_api.exceptions import *

API_BASE = "https://api.anysolver.com"

class AnySolver:
    def __init__(self, api_key):
        self.API_KEY = api_key
        
    def post(self, url, json):
        res = requests.post(f"{API_BASE}{url}", json=json, timeout=30).json()
        
        if res.get('errorId') == 1:
            raise AnySolverExternalError(f"{res.get('errorCode')}: {res.get('errorDescription')}")
        elif res.get('errorId') == 2:
            raise AnySolverInternalError(f"{res.get('errorCode')}: {res.get('errorDescription')}")

        return res
        
    def createTask(self, task: dict, settings: dict | None = None) -> str:
        data = {"clientKey": self.API_KEY, "task": task}
        if settings:
            data["settings"] = settings
            
        res = self.post("/createTask", json=data)
        return res.get("taskId")
    
    def getTaskResult(self, taskId: str) -> dict:
        data = {"clientKey": self.API_KEY, "taskId": taskId}
        res = self.post("/getTaskResult", json=data)        
        return res

    def getBalance(self) -> str:
        data = {"clientKey": self.API_KEY}
        res = self.post("/getBalance", json=data)                
        return res.get("balance")
    
    
    def solve(self, task: dict, settings: dict | None = None, timeout: int = 180, delay: int = 5) -> str:
        task_id = self.createTask(task, settings)
        
        for i in range(int(timeout / delay)):
            result = self.getTaskResult(task_id)
            status = result.get("status")
            if status == "processing":
                time.sleep(delay)
                continue
            elif status == "ready":
                return result.get("solution")
            elif status == "failed":
                raise AnySolverExternalError(f"{result.get('errorCode')}: {result.get('errorDescription')}")
            else:
                time.sleep(delay)
                continue
        
        raise AnySolverTimeoutError(f"Task {task_id} timed out")
    