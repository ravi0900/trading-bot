import argparse
import sys
from bot.orders import execute_order
from bot.validators import (
    validate_symbol, 
    validate_side, 
    validate_order_type, 
    validate_quantity, 
    validate_price,
    ValidationError
)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair symbol, e.g., BTCUSDT")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"], help="Order side (BUY/SELL)")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"], dest="order_type", help="Order type (MARKET/LIMIT)")
    parser.add_argument("--quantity", type=float, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price for LIMIT orders (required if type is LIMIT)")
    
    args = parser.parse_args()
    
    print("=== Order Request Summary ===")
    print(f"Symbol:   {args.symbol}")
    print(f"Side:     {args.side}")
    print(f"Type:     {args.order_type}")
    print(f"Quantity: {args.quantity}")
    if args.order_type == "LIMIT":
        print(f"Price:    {args.price}")
    print("=============================")
    
    try:
        # Validate inputs
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type) if args.order_type == "LIMIT" else None
        
        if order_type == "LIMIT" and price is None:
            print("Error: --price is required for LIMIT orders.")
            sys.exit(1)
            
        print("\nPlacing order...")
        result = execute_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        
        print("\n=== SUCCESS: Order Placed ===")
        print(f"Order ID:     {result.get('orderId')}")
        print(f"Status:       {result.get('status')}")
        print(f"Executed Qty: {result.get('executedQty')}")
        print(f"Avg Price:    {result.get('avgPrice')}")
        print("=============================")
        
    except ValidationError as ve:
        print(f"\n[Validation Error] {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[Execution Error] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
