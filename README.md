# Socket.IO Star Wars Movie Search Client

This Python client application is a console app that communicates with a Socket.IO server to search for Star Wars characters. Leveraging The Star Wars API, a public REST API tailored for querying information about the first 6 Star Wars films, the app enables users to perform case-insensitive searches based on partial matches.

## Overview

This client application interacts with a Socket.IO server, which provides access to The Star Wars API. It allows users to search for Star Wars movie characters by name, handling asynchronous streaming responses.

## Setup Instructions

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/hua-zeng/star-wars-movie-search-client.git
    ```

2. Navigate to the project directory:

    ```bash
    cd star-wars-movie-search-client
    ```

3. Create and activate a Python Virtual Environment:

    ```bash
    python -m venv env
    source env/bin/activate
    ```

4. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Before running the client application, ensure that the server is up and running. You can start the Docker image as the server by running the following command in a terminal:

    ```bash
    docker run -p 3000:3000 clonardo/socketio-backend
    ```

Once the server is running, open a new terminal window and navigate to the project directory. Then, execute the following command to run the client application:

    ```bash
    ./run_client.sh
    ```

Alternatively, if you prefer to activate the virtual environment manually, you can do so by running the following command:

    ```bash
    source env/bin/activate
    ```

Then, run the Python script directly:

    ```bash
    python client.py
    ```