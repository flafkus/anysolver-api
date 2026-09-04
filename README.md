# Python Wrapper for AnySolver

Unofficial API wrapper for the [AnySolver](https://anysolver.com/) service.

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
result = solver.solve(
    {
        "type": "TaskType",
        "websiteKey": "KEY",
        "websiteURL": "https://someurl.com/"
    }
)
```
For extra fields, use the documentation for the specific task on the AnySolver API.

