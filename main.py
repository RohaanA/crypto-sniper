from utils import *
import websocket
import json 
import time
import logging
import os
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

def connect_to_websocket(details):
    # Connects to the websocket and returns the connection
    print(details)
    web_socket_link = details['web-socket-link']
    ws = websocket.WebSocketApp('wss://stream.binance.com:9443/ws/', on_message=on_message)
    ws.run_forever()
    return ws

def on_message(ws, message):
    data = json.loads(message)
    # Check if the message is a new coin launch notification
    if data['e'] == 'coin.mint':
        coin_name = data['coin']
        print(f"New coin launch: {coin_name}")

def message_handler(_, message):
    # Write message to log file
    with open("log.txt", "a") as f:
        f.write(message)
    print(message)

def main():
    # client = Spot()
    # print(client.time())
    my_client = SpotWebsocketStreamClient(on_message=message_handler)
    
    # subscribe to all symbols ticker stream
    my_client.ticker()
    
    
    time.sleep(5)

    # unsubscribe
    my_client.ticker(action=SpotWebsocketStreamClient.ACTION_UNSUBSCRIBE)
    
    logging.debug("closing ws connection")
    my_client.stop()
    
    # print(client.klines("BTCUSDT", "1m"))
    # client = Spot(api_key=os.environ["BINANCE_API_KEY"], api_secret=os.environ["BINANCE_API_SECRET"])
    # Get account and balance information
    # print(client.account())
    exit()


if __name__ == '__main__':
    print('Starting bot....')
    main()