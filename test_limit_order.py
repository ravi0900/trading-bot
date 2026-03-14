import sys
import os
sys.path.append('.')
from bot.client import BinanceTestnetClient

client = BinanceTestnetClient()
try:
    print("\nTesting LIMIT with RESULT:")
    res_res = client._request("POST", "/fapi/v1/order", {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "quantity": 0.01,
        "price": 100000,
        "timeInForce": "GTC",
        "newOrderRespType": "RESULT"
    })
    print(res_res)
except Exception as e:
    print(e)
