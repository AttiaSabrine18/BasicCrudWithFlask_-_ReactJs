# Flask React Authentication App

This application is an basic example of a CRUD (Create, Read, Update, Delete) application developed using React.js for the frontend, Python Flask for the backend, and MySQL for the database. It allows managing users with basic CRUD operations on the database.
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#project-features)
- [License](#license)

## Installation

### Prerequisites

- Python 3.12.4
- Node.js v20.11.0
- npm 10.4.0

### Backend (Flask)

1. Clone the repository:

    ```sh
    git clone  https://github.com/AttiaSabrine18/BasicCrudWithFlask_-_ReactJs.git
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv env
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Create a `.env` file in the root directory and add your environment variables:

    ```sh
    touch .env
    ```

    Add the following content to the `.env` file:

    ```env
    SECRET_KEY=your_secret_key
    DATABASE_URI=your_Strin_DB_Connection
    ```
6. Run the Flask application:

    ```sh
    flask run
    ```

### Frontend (React)

1. Navigate to the `client` directory:

    ```sh
    cd frontEnd
    ```

2. Install the required packages:

    ```sh
    npm install
    ```

3. Run the React application:

    ```sh
    npm run dev
    ```

## Usage

After following the installation steps, you can access the application at `http://localhost:5173/` for the frontend and `http://127.0.0.1:5000` for the backend API.

### License
MIT License
## Features
User List: Displays all existing users.
Add New User: Allows adding a new user to the database.
Update User: Enables updating information of an existing user.
Delete User: Allows deleting a user from the database.

