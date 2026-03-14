import sys
import os
sys.path.append('.')
from bot.client import BinanceTestnetClient

client = BinanceTestnetClient()
try:
    print("Testing with ACK:")
    res_ack = client._request("POST", "/fapi/v1/order", {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "MARKET",
        "quantity": 0.01,
        "newOrderRespType": "ACK"
    })
    print(res_ack)

    print("\nTesting with RESULT:")
    res_res = client._request("POST", "/fapi/v1/order", {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "MARKET",
        "quantity": 0.01,
        "newOrderRespType": "RESULT"
    })
    print(res_res)
except Exception as e:
    print(e)
