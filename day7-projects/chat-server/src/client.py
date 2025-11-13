"""Async Chat Client - TODO Implementation"""
import asyncio

class ChatClient:
    """TODO: Async chat client"""
    def __init__(self, host='127.0.0.1', port=8888):
        """TODO: Initialize client"""
        self.host = host
        self.port = port
    
    async def send_message(self, writer, message):
        """TODO: Send message to server"""
        pass
    
    async def receive_messages(self, reader):
        """TODO: Receive messages from server"""
        pass
    
    async def connect(self):
        """TODO: Connect to server"""
        pass

async def main():
    """TODO: Run client"""
    pass

if __name__ == "__main__":
    asyncio.run(main())
