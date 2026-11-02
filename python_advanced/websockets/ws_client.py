#!/usr/bin/env python3
import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    """Send one message to a Websocket server and return its reply.

    Args:
        uri: address of the server.
        text: message to send.

    Returns:
        message received from the server.
    """

    async with connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
    return response


async def main():
    """Send "Hello WebSocket" to the echo server and print the reply."""
    response = await connect_and_send("ws://127.0.0.1:8765", "Hello WebSocket")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
