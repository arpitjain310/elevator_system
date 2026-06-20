# Elevator System API

A Django REST Framework API that simulates a multi-elevator system. It manages a fleet of elevators and exposes endpoints to dispatch floor requests, query the next destination and movement state, control the doors, and flag an elevator for maintenance.

## Tech stack

- Python 3.10+
- Django 4.2
- Django REST Framework

## Getting started

```bash
git clone https://github.com/arpitjain310/elevator_system.git
cd elevator_system

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API is served under `http://localhost:8000/api/`.

`SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` are read from the environment (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`); development defaults apply when they are unset.

## Quick example

```bash
# Create a system with 3 elevators
curl -X POST http://localhost:8000/api/elevator-system/ \
  -H "Content-Type: application/json" -d '{"number_of_elevators": 3}'

# Add a floor request to elevator 1
curl -X POST http://localhost:8000/api/elevators/1/save_request/ \
  -H "Content-Type: application/json" -d '{"floor": 7}'

# Ask where elevator 1 goes next
curl http://localhost:8000/api/elevators/1/next_destination/
```

## API endpoints

1. **Initialize the elevator system**
   - `POST /api/elevator-system/`
   - Body: `{ "number_of_elevators": 5 }`
   - Response: `{ "message": "Elevator system initialized with 5 elevators" }`

2. **Fetch all requests for an elevator**
   - `GET /api/elevators/{elevator_id}/requests/`
   - Response: `[ { "id": 1, "floor": 3 }, { "id": 2, "floor": 5 } ]`

3. **Fetch the next destination floor**
   - `GET /api/elevators/{elevator_id}/next_destination/`
   - Response: `{ "next_destination": 4 }`

4. **Check whether the elevator is moving**
   - `GET /api/elevators/{elevator_id}/is_moving_up/`
   - Response: `{ "is_moving_up": true }`

5. **Save a user request**
   - `POST /api/elevators/{elevator_id}/save_request/`
   - Body: `{ "floor": 7 }`
   - Response: `{ "message": "Request saved successfully" }`

6. **Mark an elevator as not working / in maintenance**
   - `POST /api/elevators/{elevator_id}/mark_not_working/`
   - Response: `{ "message": "Elevator marked as not working" }`

7. **Open the door**
   - `POST /api/elevators/{elevator_id}/open_door/`
   - Response: `{ "message": "Door opened" }`

8. **Close the door**
   - `POST /api/elevators/{elevator_id}/close_door/`
   - Response: `{ "message": "Door closed" }`

## Running the tests

```bash
python manage.py test
```

## Scope and simplifications

This models elevator state and request dispatch, not a real-time control loop:

- `next_destination` returns the lowest pending request floor. A production scheduler would also account for the car's current direction (the SCAN algorithm).
- Elevator movement is represented as stored state (`current_floor`, `is_moving`) rather than advanced by a background simulation, so those fields reflect explicitly set values.
