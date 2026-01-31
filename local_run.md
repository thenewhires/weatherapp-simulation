# Running the Weather App Locally

## Prerequisites

*   Python 3.6+
*   Node.js 14+
*   npm or yarn

## Steps

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd weatherapp-simulation
    ```

2.  **Backend Setup (Flask):**

    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    Set the OPENWEATHER_API_KEY environment variable (replace YOUR_API_KEY with your actual API key):
    ```bash
    export OPENWEATHER_API_KEY=YOUR_API_KEY
    python app.py
    ```

3.  **Frontend Setup (React):**

    ```bash
    cd ../frontend
    npm install
    npm start
    ```

4.  **Access the Application:**

    Open your browser and go to `http://localhost:3000`.

## Notes

*   Make sure the backend is running before starting the frontend.
*   Replace `YOUR_API_KEY` with your actual OpenWeatherMap API key in the `app.py` file and set the environment variable.
