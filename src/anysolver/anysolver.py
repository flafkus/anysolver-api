from typing import Optional
from anysolver.exceptions import AnySolverInternalError, AnySolverExternalError
from enum import Enum
import time

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
        
        if res.get('errorId') == 1:
            raise AnySolverExternalError(f"{res.get('errorCode')}: {res.get('errorDescription')}")
        elif res.get('errorId') == 2:
            raise AnySolverInternalError(f"{res.get('errorCode')}: {res.get('errorDescription')}")
        
        return res
    
    def getTaskResult(self, taskId: str) -> str:
        data = {"clientKey": self.API_KEY, "taskId": taskId}
        res = requests.post(f"{API_BASE}/getTaskResult", json=data).json()
        
        if res.get('errorId') == 1:
            raise AnySolverExternalError(f"{res.get('errorCode')}: {res.get('errorDescription')}")
        elif res.get('errorId') == 2:
            raise AnySolverInternalError(f"{res.get('errorCode')}: {res.get('errorDescription')}")
        
        return res

    def getBalance(self) -> str:
        data = {"clientKey": self.API_KEY}
        res = requests.post(f"{API_BASE}/getBalance", json=data).json()  
          
        if res.get('errorId') == 1:
            raise AnySolverExternalError(f"{res.get('errorCode')}: {res.get('errorDescription')}")
        elif res.get('errorId') == 2:
            raise AnySolverInternalError(f"{res.get('errorCode')}: {res.get('errorDescription')}")
        
        return res
    
    
    def solve(self, task: dict, settings: Optional[dict] = None, timeout: int = 180, delay: int = 5) -> str:
        created_task = self.createTask(task, settings)
        print(created_task)
        task_id = created_task.get("taskId")
        
        for i in range(int(timeout / delay)):
            result = self.getTaskResult(task_id)
            status = result.get("status")
            if status == "processing":
                time.sleep(delay)
                continue
            elif status == "ready":
                return result.get("solution")
            elif status == "failed":
                raise AnySolverExternalError(f"{result}: {result.get('errorDescription')}")
        
        print(f"Task {task_id} timed out")
        return
    