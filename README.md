# Binance Futures Testnet Trading Bot

A simplified Python trading bot to place Market and Limit orders on the Binance Futures Testnet (USDT-M).

## Requirements

- Python 3.x
- `requests` library

## Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository_url>
   cd trading_bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Credentials**:
   To interact with the Binance Futures Testnet, you need to set your API key and secret. Provide them in a `.env` file at the root of the project.
   
   ```bash
   cp .env.example .env
   # Edit .env and paste your credentials
   ```

## Usage

The application provides a clean command-line interface (CLI) to place orders.

```bash
python3 cli.py --symbol <SYMBOL> --side <BUY|SELL> --type <MARKET|LIMIT> --quantity <QTY> [--price <PRICE>]
```

### Examples

**1. Place a MARKET BUY order for BTCUSDT (Quantity: 0.01)**
```bash
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**2. Place a LIMIT SELL order for BTCUSDT (Quantity: 0.05, Price: 95000)**
```bash
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.05 --price 95000
```

## Features
- **Validation**: Checks inputs for valid symbols, matching types, positive amounts, etc.
- **Logging**: Automatically logs all request and response details to `trading_bot.log` as well as the console. Rotating log handlers are used to prevent file bloat.
- **Error Handling**: Graceful fallback and error descriptions for API and network issues.

## Assumptions
- The testnet base URL used is `https://testnet.binancefuture.com`.
- Time-in-Force for LIMIT orders is set by default to `GTC` (Good Till Cancel).
- The user has sufficient testnet balance for the orders.
