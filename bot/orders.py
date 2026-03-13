from .client import BinanceTestnetClient
from .logging_config import setup_logger

logger = setup_logger("bot.orders")

def execute_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """
    Executes a market or limit order via the Binance Testnet client.
    Returns a standardized dictionary with order details.
    """
    try:
        client = BinanceTestnetClient()
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        
        # Expected response structure from Binance Futures New Order
        order_details = {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice")
        }
        
        logger.info(f"Order executed successfully: {order_details}")
        return order_details
        
    except Exception as e:
        logger.error(f"Failed to execute order: {e}")
        raise
