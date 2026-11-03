#!/usr/bin/env python3
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    """Return the home page."""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(connection):
    """Echo every message received on /ws."""
    await connection.accept()

    async for message in connection.iter_text():
        await connection.send_text(message)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
