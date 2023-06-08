import asyncio
import websockets

async def handle_websocket(websocket, path):
    # Handle incoming WebSocket messages
    # print("In handle_websocket, beginning: ")
    async for message in websocket:
        # Send a response back to the client
        response = "Received: " + message
        await websocket.send(response)

if __name__ == '__main__':
    print("In main")
    start_server = websockets.serve(handle_websocket, 'localhost', 8765)

    # Start the WebSocket server
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
