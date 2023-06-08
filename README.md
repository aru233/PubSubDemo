A basic demo of a pub sub system with notifications using Redis and Websockets and Python.
A new message is published by the publisher to a specific topic in the pub/sub system (here, Redis).
All subscribers of the topic are notified of every new message in the topic they are subscribed to via websocket connections.

## Installation Instructions
In a virtual environment, 
Install relevant packages via
```
pip install websockets redis
```

## Running the code
We have 3 processes running in 3 separate terminals
-> The websocket server: 
```
python3 src/websocketServer.py
```
-> The publisher: 
```
python3 src/publisher.py
```
-> The subscriber: 
```
python3 src/subscriber.py
```



(Subscriber waits for user to enter the message to be published)

To extend the scope of the system (as part of a document sharing/collaboration system), we can use a relational database to store user information,d ocument-related information for imposing privilege restrictions etc.

We’ll employ a relational database for saving users’ information and document-related information for imposing privilege restrictions. 

Notifications are asynchronous operations; we can use the queue (through a pub-sub component) as demonstrated in the code. The API gateway generates these requests and forwards them to the pub-sub module. Users sharing documents can generate notifications through this process.