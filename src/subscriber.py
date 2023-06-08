import asyncio
import json
import websockets
import redis

async def subscribe(topic):
    # Redis pub/sub logic
    r = redis.Redis()
    p = r.pubsub()
    p.subscribe(topic)
    
    # Subscriber connects to the WebSocket server at ws://localhost:8765
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(json.dumps({'subscribe': topic})) # Subscriber subscribes to a specific topic by sending a JSON payload with the subscribe key

        # Subscriber continuously listens for incoming messages from the server
        while True:
            message = p.get_message()
            print("The message is:", message)

            # Wait for a response from the WebSocket server
            response = await websocket.recv()
            print(f'Received message on topic {topic}: {response}')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(subscribe('topic1'))
    asyncio.get_event_loop().run_forever()

'''
Typically a subscriber would not need separate WebSocket connections for each topic they are subscribed to in a pub/sub system. 
Instead, a single WebSocket connection can be used to receive messages for multiple topics.
In a WebSocket-based pub/sub system, the subscriber can send a message to the server indicating the topics they want to subscribe to. 
The server then manages the subscriptions and sends relevant messages over the existing WebSocket connection to the subscriber.
'''