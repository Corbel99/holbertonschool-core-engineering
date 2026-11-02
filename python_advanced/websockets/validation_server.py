#!/usr/bin/env python3
import asyncio
from websockets.exceptions import ConnectionClosed
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    """Validate each message and reply OK or ERR.

    Args:
        websocket: connection with the client.
    """
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """Start the validation server and keep it running."""
    server = await serve(connection_handler, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
