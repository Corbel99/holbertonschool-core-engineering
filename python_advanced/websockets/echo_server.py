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
