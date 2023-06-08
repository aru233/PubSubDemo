import asyncio
import websockets
import redis
import json

async def publish(topic):
    r = redis.Redis()
    print("In publish, beginning")

    # Publisher connects to the WebSocket server at ws://localhost:8765
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            message = input("Enter message to publish: ")
            r.publish(topic, message) # Publish the message to Redis pub/sub

            # Publisher sends msg to server as a JSON payload containing the topic and message.
            data = {
                'topic': topic,
                'message': message
            }
            await websocket.send(json.dumps(data)) # Send a response back to the client

            # Wait for a response from the WebSocket server
            response = await websocket.recv()
            print("Received response:", response)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(publish('topic1'))
    asyncio.get_event_loop().run_forever()
