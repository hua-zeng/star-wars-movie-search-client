import socketio
import asyncio

# Create a Socket.IO client enabling reconnection
sio = socketio.AsyncClient(reconnection=True)


# Function to send queries with the required payload structure
async def send_query(query_text):
    # Construct the object payload
    query_payload = {'query': query_text}
    print(f"Searching for {query_text} ...")
    await sio.emit('search', query_payload)


# Function to handle user input
async def handle_user_input():
    try:
        # Utilize asyncio to handle input non-blocking
        query_text = await asyncio.to_thread(input, "What character would you like to search for (or type 'exit' to quit): ")
        if query_text.lower() == 'exit':
            print("Exiting...")
            await sio.disconnect()  # Disconnects the client and exits the program
        else:
            await send_query(query_text)
    except KeyboardInterrupt:  # Catch KeyboardInterrupt (Ctrl+C)
        print("\nCtrl-C detected. Exiting...")
        await sio.disconnect()  # Disconnects the client and exits the program
    except EOFError:  # Catch EOFError (Ctrl+D)
        print("\nCtrl-D detected. Exiting...")
        await sio.disconnect()  # Disconnects the client and exits the program


# Event handler for successful connection
@sio.event
async def connect():
    print("-- connected to the server")
    await handle_user_input()  # Call once on connect to start the interaction


# Event handler for handling messages received on the 'search' event
@sio.on('search')
@sio.on('search')
async def on_search(data):
    # Handle error response if no matching result is found
    if 'error' in data:
        print("Error:", data['error'])
    # Process successfully received and matched data
    else:
        print(f"({data['page']}/{data['resultCount']}) {data['name']} - [{data['films']}]")

    # Check if all results have been received and call for a new search
    if data['page'] == data['resultCount']:
        await handle_user_input()


# Event handler for disconnection
@sio.event
async def disconnect():
    print("Disconnected from server.")


# Event handler for connection error
@sio.event
async def connect_error():
    print("Connection failed.")


async def start_client():
    try:
        await sio.connect('http://localhost:3000')
        await sio.wait()  # Wait for the disconnect to be called and completed.
    finally:
        await sio.disconnect()  # Ensure disconnect is called to clean up.


if __name__ == "__main__":
    asyncio.run(start_client())
