#!/usr/bin/env python3
import asyncio
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    """Send back every message received from a client

    Args:
        websocket: connection with the client.
    """

    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the echo server and keep it running."""
    server = await serve(connection_handler, "127.0.0.1", 8765)
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
