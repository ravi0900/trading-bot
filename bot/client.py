import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
import os
from dotenv import load_dotenv
from .logging_config import setup_logger

load_dotenv()

logger = setup_logger("bot.client")

class BinanceTestnetClient:
    BASE_URL = "https://testnet.binancefuture.com"
    
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET")
        
        if not self.api_key or not self.api_secret:
            logger.error("API credentials missing")
            raise ValueError("BINANCE_API_KEY and BINANCE_API_SECRET must be set")
            
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    def _get_timestamp(self):
        return int(time.time() * 1000)

    def _sign_payload(self, payload):
        query_string = urlencode(payload)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        return signature

    def _request(self, method, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        params = params or {}
        
        # Add timestamp and signature for signed endpoints
        params['timestamp'] = self._get_timestamp()
        params['signature'] = self._sign_payload(params)
        
        try:
            logger.debug(f"Sending {method} request to {url}")
            if method == "GET":
                response = self.session.get(url, params=params)
            elif method == "POST":
                # Binance Futures Testnet accepts params in query string or body depending on endpoint
                # New order endpoint uses params (query string format even over POST) or form-data
                response = self.session.post(url, params=params)
            else:
                raise ValueError(f"Unsupported method: {method}")
                
            response.raise_for_status()
            data = response.json()
            logger.debug(f"Response data: {data}")
            return data
            
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
            raise Exception(f"Binance API Error: {e.response.text}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Network Error: {e}")
            raise Exception(f"Network Error: {str(e)}")
            
    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"
        
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }
        
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC" # Good Till Cancel

        logger.info(f"Placing {side} {order_type} order for {quantity} {symbol}")
        
        return self._request("POST", endpoint, params)
