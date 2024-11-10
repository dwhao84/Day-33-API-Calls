# ISS Position Tracker

This Python script demonstrates how to fetch the current position of the International Space Station (ISS) using the Open Notify API.

## Features

- Fetches real-time ISS position data
- Extracts longitude and latitude coordinates
- Handles API response status codes
- Returns coordinates as a tuple

## Prerequisites

```python
import requests
```

## Usage

The script performs the following operations:

1. Makes an API request to fetch ISS position data:
```python
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
```

2. Validates the API response:
```python
response.raise_for_status()
```

3. Extracts position data:
```python
iss_position_data = response.json()['iss_position']
longitude = response.json()['iss_position']["longitude"]
latitude = response.json()['iss_position']["latitude"]
```

4. Returns the position as a tuple:
```python
iss_position = (longitude, latitude)
```

## Error Handling

The script includes two methods for error handling:

1. Using `raise_for_status()` to automatically raise exceptions for bad HTTP responses
2. (Commented example) Manual status code checking:
```python
if response.status_code == 404:
    raise Exception(f"That status code is { 404 }")
elif response.status_code == 401:
    raise Exception(f"That status code is { 401 }")
```

## API Reference

- Endpoint: `http://api.open-notify.org/iss-now.json`
- Method: GET
- Response Format: JSON
- Expected Response Structure:
```json
{
    "iss_position": {
        "longitude": "string",
        "latitude": "string"
    }
}
```

## Notes

- All position coordinates are returned as strings
- No authentication is required for this API
- Response status code 200 indicates successful request