#!/usr/bin/env python3
import asyncio
from websockets.exceptions import ConnectionClosed
from websockets.asyncio.server import serve

connected_clients = set()


async def connection_handler(websocket):
    """Send each message to all connected clients, prefixed with B:.

    Args:
        websocket: connection with the client.
    """
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for connection in set(connected_clients):
                try:
                    await connection.send(f"B:{message}")
                except ConnectionClosed:
                    pass
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    """Start the broadcast server and keep it running."""
    server = await serve(connection_handler, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())

