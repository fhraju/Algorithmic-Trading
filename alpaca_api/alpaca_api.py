import alpaca_trade_api as tradeapi
import os


SEC_KEY = os.environ.get('sec_key') # Enter Your Secret Key Here
PUB_KEY = os.environ.get('api_key_id') # Enter Your Public Key Here

print(SEC_KEY)
# BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading
# api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL) # For real trading, don't enter a base_url