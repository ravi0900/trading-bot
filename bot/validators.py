class ValidationError(Exception):
    pass

def validate_symbol(symbol: str) -> str:
    symbol = symbol.strip().upper()
    if not symbol.isalnum():
        raise ValidationError(f"Invalid symbol format: {symbol}")
    return symbol

def validate_side(side: str) -> str:
    side = side.strip().upper()
    if side not in ["BUY", "SELL"]:
        raise ValidationError(f"Invalid side: {side}. Must be BUY or SELL.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.strip().upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValidationError(f"Invalid order type: {order_type}. Must be MARKET or LIMIT.")
    return order_type

def validate_quantity(quantity: float) -> float:
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError
        return qty
    except ValueError:
        raise ValidationError(f"Invalid quantity: {quantity}. Must be a positive number.")

def validate_price(price: float, order_type: str) -> float:
    if order_type == "MARKET":
        return 0.0
    try:
        p = float(price)
        if p <= 0:
            raise ValueError
        return p
    except ValueError:
        raise ValidationError(f"Invalid price: {price}. Must be a positive number for LIMIT orders.")
