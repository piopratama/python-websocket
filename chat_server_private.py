import asyncio
from websockets.asyncio.server import serve

# Store connected clients with their usernames
connected_clients = {}

async def handle_client(websocket):
    # Register the client with their username
    try:
        await websocket.send("Enter your username:")
        username = await websocket.recv()

        if username in connected_clients:
            await websocket.send("Username already taken. Disconnecting.")
            return

        connected_clients[username] = websocket
        print(f"{username} connected.")

        await websocket.send("Connected! Use @username <message> to send a private message.")

        # Handle messages
        async for message in websocket:
            if message.startswith("@"):
                # Extract target username and the private message
                try:
                    target_username, private_message = message[1:].split(" ", 1)
                    target_client = connected_clients.get(target_username)

                    if target_client:
                        await target_client.send(f"Private from {username}: {private_message}")
                    else:
                        await websocket.send(f"User {target_username} is not connected.")
                except ValueError:
                    await websocket.send("Invalid format. Use @username <message>.")
            else:
                # Broadcast to all clients
                for client in connected_clients.values():
                    if client != websocket:
                        await client.send(f"{username}: {message}")
    except asyncio.CancelledError:
        print(f"{username} disconnected.")
    finally:
        # Unregister client on disconnect
        if username in connected_clients:
            del connected_clients[username]

async def main():
    async with serve(handle_client, "localhost", 6789):
        print("Private chat server running on ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
