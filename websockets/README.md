# Real-time communication with WebSockets

This project is part of the Holberton School Core Engineering curriculum (`python_advanced/websockets`).

## Description

Traditional HTTP follows a request–response model: the client asks, the server answers. WebSockets keep a persistent, bidirectional connection open, so both the client and the server can send messages at any time. This project builds a real-time communication system step by step with Python's `websockets` library and `asyncio`.

## Learning Objectives

- Implement a WebSocket server using asynchronous programming
- Handle multiple concurrent client connections
- Send and receive messages in real time
- Implement different message exchange patterns
- Enforce a defined message format when required

## Requirements

- All files start with `#!/usr/bin/env python3`
- All files end with a new line
- Code follows PEP8
- Uses the `websockets` library and `async` / `await`
- The server binds to `127.0.0.1` (IPv4)

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `echo_server.py` | WebSocket server on port 8765 that echoes every text message back to its sender |

## Usage

```bash
./echo_server.py
websockets ws://localhost:8765/
```

## Author

Thomas — Holberton School
