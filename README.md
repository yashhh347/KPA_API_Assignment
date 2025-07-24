# KPA API Assignment

## Technologies Used:

- FastAPI
- PostgreSQL
- SQLAlchemy
- Python-dotenv

## Setup:

1. Clone repo / unzip folder
2. Create virtual env and activate
3. Install dependencies from `requirements.txt`
4. Create PostgreSQL DB named `kpa_assignment`
5. Run server: `uvicorn main:app --reload`

## APIs Implemented:

1. `POST /personal-details` — Create user info
2. `GET /personal-details/{id}` — Get user info by ID

## Assumptions:

- No auth added
- Simple validation only
