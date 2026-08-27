# URL Shortener

A lightweight, full-stack web application that converts long URLs into compact, easy-to-share links. Built for Task 2 of the club selection process.

## Tech Stack
* **Backend:** Python, Flask
* **Database:** SQLite (built-in, serverless)
* **Frontend:** HTML5, CSS3 

## Core Features & Requirements Met
* **Unique Link Generation:** Uses Python's `random` and `string` libraries to generate a unique 6-character alphanumeric code for every submitted URL.
* **Instant Redirection:** Dynamic Flask routing intercepts the short code, queries the database, and instantly redirects the user to the original destination.
* **Robust Validation:** Handles invalid or empty inputs on both the frontend (HTML5 `type="url"`) and backend (verifying `http://` or `https://` prefixes) to prevent database errors.
* **Environment Agnostic:** Utilizes `request.host_url` to dynamically build the shortened link based on the current hosting environment (e.g., localhost during testing, or a live domain in production).

## Developer Approach & Explanation
I chose a **Flask + SQLite** architecture to create a production-ready but highly portable application. 
Rather than keeping the URL mappings in volatile memory (which resets when the server restarts), I implemented a serverless SQLite database. This ensures the data persists between sessions, but still packages the entire database into a single `.db` file. This allows reviewers to download the repository and test the application immediately without needing to configure a local SQL server.

## How to Run Locally

1. Ensure Python is installed on your machine.
2. Clone this repository or extract the ZIP file.
3. Open your terminal in the project directory.
4. Install Flask if you haven't already:
   ```bash
   pip install flask
