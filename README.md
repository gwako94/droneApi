## API Spec
The preferred JSON object to be returned by the API should be structured as follows:

### Drone (for registration)

```source-json
{
    "drone": {
        "serial_number": "dr1267qwerty",
        "model": "Lightweight",
        "weight_limit": 350.0,
        "battery_capacity": 100.0,
        "state": "idle",
        "created_at": "2021-12-29T06:38:51.806461Z"
    },
    "message": "Drone registered successfully"
}

```
### Loading drone with medication
```source-json
{
    "Medication": {
        "name": "medication2",
        "weight": 100.0,
        "code": "CRS50",
        "image": "https://sample-image",
        "drone": 1
    },
    "message": "Successfully loaded drone with medication"
}

```
### Check loaded medication for a given drone
```source-json
{
    "Medication": [
        {
            "name": "medication2",
            "weight": 100.0,
            "code": "CRS50",
            "image": "https://sample-image",
            "drone": {
                "serial_number": "dr1267qwert2y",
                "model": "Lightweight",
                "weight_limit": 350.0,
                "battery_capacity": 100.0,
                "state": "idle",
                "created_at": "2021-12-29T06:59:46.800679Z"
            }
        },
        {
            "name": "medication2",
            "weight": 100.0,
            "code": "CRS50",
            "image": "https://sample-image",
            "drone": {
                "serial_number": "dr1267qwert2y",
                "model": "Lightweight",
                "weight_limit": 350.0,
                "battery_capacity": 100.0,
                "state": "idle",
                "created_at": "2021-12-29T06:59:46.800679Z"
            }
        }
    ],
    "message": "Successfully fetched drone loaded medication"
}
```
### Check Available drones 
```source-json
{
    "Drones": [
        {
            "serial_number": "dr1267qwert2y",
            "model": "Lightweight",
            "weight_limit": 350.0,
            "battery_capacity": 100.0,
            "state": "idle",
            "created_at": "2021-12-29T06:59:46.800679Z"
        }
    ],
    "message": "Succesfully fetched all available drones"
}
```
### Check drones battery level
```source-json
{
    "Battery Capacity": {
        "battery_capacity": 100.0
    },
    "message": "Successfully fetched drone battery level"
}
```
Endpoints:
----------

### Drone Registration:

`POST /api/drone/register`

Example request body:

```source-json
{
    "serial_number": "dr1267qwerty",
    "model": "Lightweight",
    "weight_limit": 350,
    "battery_capacity": 100.0,
    "state": "idle"
}
```

returns a Drone

Required fields: `serial_number`, `weight_limit`, `battery_capacity`

### Load drone with medication:

`POST /api/drone/loading/<serial_number>`

Example request body:

```source-json
{
    "name": "medication2",
    "weight": 100.0,
    "code": "CRS50",
    "image": "https://sample-image"  
}
```

returns a laoded medication

Required fields: `name`, `weight`, `code`, `image`

### Get loaded medication for a given drone

`GET /api/drone/loads/dr1267qwert2y`

returns all loaded medication for the given drone


### Get available drones

`GET /api/drone/available`

returns all available drone

### Get a drone's battery level

`GET /api/drone/battery_level/<serial_number>`

returns a specific drone's battery level



