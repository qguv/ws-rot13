#!/usr/bin/env python3

import asyncio
import codecs
import websockets

async def handle(websocket, path):
    print(f'client connected from {websocket.remote_address[0]}')
    try:
        async for message in websocket:
            rot13 = codecs.encode(message, 'rot_13')
            print(f'"{message}" -> "{rot13}"')
            await websocket.send(rot13)
    except websockets.exceptions.ConnectionClosed:
        print(f'lost connection to {websocket.remote_address[0]}')

start_server = websockets.serve(handle, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
