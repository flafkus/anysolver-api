# Python Wrapper for AnySolver

Unofficial API wrapper for the [AnySolver](https://anysolver.com/) service.

## Requirements
- Python 3.12

## Installation
```
pip install anysolver-api
```

or

```
uv add anysolver-api
```

## Usage
```py
from anysolver_api import AnySolver

solver = AnySolver("API_KEY")

balance = solver.getBalance()
print(f"Balance: ${balance}")

result = solver.solve(
    {
        "type": "TaskType",
        "websiteKey": "KEY",
        "websiteURL": "https://someurl.com/"
    }
)['token']
```
For extra fields, use the documentation for the specific task on the AnySolver API.

You can also provide extra settings, e.g. for routing through specific models / auto route settings:
```py
result = solver.solve(
    task = {
        "type": "TaskType",
        "websiteKey": "KEY",
        "websiteURL": "https://someurl.com/"
    },
    settings = {
        "routing": { "mode": "autoCheapest" }
    },
    timeout = 120, # how long to wait for solution
    delay = 5 # time between checks
)['token']
```

## Error handling

All API errors raise one of the following:
```py
from anysolver_api.exceptions import AnySolverExternalError, AnySolverInternalError, AnySolverTimeoutError

try:
    result = solver.solve({...})
except AnySolverExternalError as e:
    # invalid input, bad task, etc.
    ...
except AnySolverInternalError as e:
    # error on AnySolver's side
    ...
except AnySolverTimeoutError as e:
    # task didn't finish in time
    ...
```