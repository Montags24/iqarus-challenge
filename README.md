# ResQHub

ResQHub is a progressive web application designed to enable individuals and teams to quickly assess on-ground conditions following emergencies such as natural disasters. The app is built using Vue.js for the frontend, Flask for the backend, and PostgreSQL for the database.

## Features

- Rapid condition assessment after emergencies
- User-friendly interface for data entry and review
- Real-time data synchronization across devices
- Offline capabilities for field use

## Technologies Used

- **Frontend**: Vue.js
- **Backend**: Flask
- **Database**: PostgreSQL
- **PWA**: Progressive Web App features for offline access and mobile usage

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Node.js (v18 or higher)
- Python (v3.11 or higher)
- PostgreSQL (v15 or higher)
- npm (v9 or higher)
- pip (v20 or higher)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Montags24/iqarus-challenge.git
   cd iqarus-challenge
   code .
    ```
2. **Set up the backend:**
    ```sh
   cd backend
    ```
    Create and activate a virtual environment:
    ```sh
    python3.11 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
    Set up environment variables:
    ```sh
    cp template.env .env # On Windows, use `copy template.env .env`
    ```
    Update .env with your Postgres Database details
    ```sh
    DB_TYPE = postgresql
    DB_PASSWORD = 
    DB_USERNAME = 
    DB_ADDRESS = localhost
    DB_PORT = 5432
    DB_NAME = 
    ```
    Set up the PostgreSQL database with SQLAlchemy:
    ```sh
    flask db upgrade
    ```
    Run the flask app:
    ```sh
    flask run
    ```
2. **Set up the frontend:**\
    In a new terminal from root directory:
    ```sh
    cd frontend
    ```
    Install the required npm packages:
    ```sh
    npm install
    ```
    run the Vue development server
    ```sh
    npm run dev
    ```

## Running the App
- Open your browser and navigate to http://localhost:5173 to see the frontend.
- The backend API will be running at http://localhost:5000.