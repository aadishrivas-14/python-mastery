# Project 5: Async Chat Server

Build an asynchronous TCP chat server supporting multiple clients.

## Features
- Multiple concurrent clients
- Broadcast messages to all clients
- Private messaging
- Username registration
- Connection/disconnection notifications

## Usage
```bash
# Start server
python server.py --port 8888

# Connect client
python client.py --host localhost --port 8888
```

## Implementation
- asyncio for async I/O
- TCP sockets
- Message protocol
- Client management
- Error handling

## Run
```bash
python src/server.py
python src/client.py  # In another terminal
pytest tests/ -v
```
