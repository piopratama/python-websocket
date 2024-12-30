import asyncio
from websockets.asyncio.server import serve

# Store all connected clients
connected_clients = set()

async def handle_client(websocket):
    # Register the client
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to all other clients
            for client in connected_clients:
                if client != websocket:  # Don't send the message back to the sender
                    await client.send(message)
    except asyncio.CancelledError:
        print("Client disconnected.")
    finally:
        # Unregister the client
        connected_clients.remove(websocket)

async def main():
    async with serve(handle_client, "localhost", 6789) as server:
        print("WebSocket server is running on ws://localhost:6789")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
