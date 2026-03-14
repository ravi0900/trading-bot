# Binance Futures Testnet Trading Bot

A simplified Python trading bot to place Market and Limit orders on the Binance Futures Testnet (USDT-M).

## Requirements

- Python 3.x
- `requests` library

## Setup

1. **Clone the repository** (or navigate to your project directory):
   ```bash
   cd trading_bot
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API keys**:
   - Copy `.env.example` to a new file named `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and configure your `BINANCE_API_KEY` and `BINANCE_API_SECRET`.

## Usage

This project supports both a modern graphical interface and a command-line interface.

### Web UI (Recommended)
You can start a lightweight web server that provides a clean, fast dashboard for executing orders:

```bash
python app.py
```
*Then open `http://localhost:5000` in your web browser.*

### Command-Line Interface
Alternatively, run the script from the command line using `bot/cli.py`:

```bash
python -m bot.cli --symbol <SYMBOL> --side <BUY|SELL> --type <MARKET|LIMIT> --quantity <QTY> [--price <PRICE>]
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
