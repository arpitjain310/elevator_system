# Elevator System API

## Overview

This repository contains Django-based API that simulates an elevator system. The system allows the management of multiple elevators and provides endpoints to perform various operations related to elevator control.

## Features

- Initialize the elevator system with a specified number of elevators.
- Fetch requests, next destination, and current movement status for a given elevator.
- Save user requests to the list of requests for an elevator.
- Mark an elevator as not working or in maintenance.
- Open and close the elevator door.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework


# Elevator System API

## API Endpoints

1. **Initialize Elevator System**
   - *Endpoint:* `POST /api/elevator-system/initialize/`
   - *Request Body (JSON):*
     ```json
     {
         "number_of_elevators": 5
     }
     ```
   - *Response (JSON):*
     ```json
     {
         "message": "Elevator system initialized with 5 elevators"
     }
     ```

2. **Fetch All Requests for a Given Elevator**
   - *Endpoint:* `GET /api/elevators/{elevator_id}/requests/`
   - *Response (JSON):*
     ```json
     [
         {
             "id": 1,
             "floor": 3
         },
         {
             "id": 2,
             "floor": 5
         }
     ]
     ```

3. **Fetch Next Destination Floor for a Given Elevator**
   - *Endpoint:* `GET /api/elevators/{elevator_id}/next_destination/`
   - *Response (JSON):*
     ```json
     {
         "next_destination": 4
     }
     ```

4. **Fetch If the Elevator is Moving Up or Down Currently**
   - *Endpoint:* `GET /api/elevators/{elevator_id}/is_moving_up/`
   - *Response (JSON):*
     ```json
     {
         "is_moving_up": true
     }
     ```

5. **Save User Request to the List of Requests for an Elevator**
   - *Endpoint:* `POST /api/elevators/{elevator_id}/save_request/`
   - *Request Body (JSON):*
     ```json
     {
         "floor": 7
     }
     ```
   - *Response (JSON):*
     ```json
     {
         "message": "Request saved successfully"
     }
     ```

6. **Mark an Elevator as Not Working or in Maintenance**
   - *Endpoint:* `POST /api/elevators/{elevator_id}/mark_not_working/`
   - *Response (JSON):*
     ```json
     {
         "message": "Elevator marked as not working"
     }
     ```

7. **Open the Door**
   - *Endpoint:* `POST /api/elevators/{elevator_id}/open_door/`
   - *Response (JSON):*
     ```json
     {
         "message": "Door opened"
     }
     ```

8. **Close the Door**
   - *Endpoint:* `POST /api/elevators/{elevator_id}/close_door/`
   - *Response (JSON):*
     ```json
     {
         "message": "Door closed"
     }
     ```

We can use these API endpoints to interact with the Elevator System.