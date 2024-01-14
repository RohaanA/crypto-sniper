from utils import *
import websocket
import json 
from binance.spot import Spot 
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

def main():
    client = Spot()
    print(client.time())
    
    
    # print(client.klines("BTCUSDT", "1m"))
    client = Spot(api_key='cgFX50x79EIidvJjoLiHAh257rmL11Y1MfSfigJvHtWrIEqQmAiuI8Uwo0O2HS2E', api_secret='mHoUxANkpeUipcw1p1EpamsD91fQflZ9v5KSIYtjXGIgLXgUOZ0X7eINpEjp8JpM')
    # Get account and balance information
    print(client.account())
    exit()
    chosen_exchange = "binance"
    print("Fetching configuration details from config.yaml")
    details = fetch_details(chosen_exchange)
    print(details)
    print("Connecting to the binance web socket")
    ws = connect_to_websocket(details)
    pass

if __name__ == '__main__':
    print('Starting bot....')
    main()