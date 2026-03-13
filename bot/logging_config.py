import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name="trading_bot", log_file="trading_bot.log", level=logging.INFO):
    """
    Configure a logger that writes to both the console and a rotating log file.
    """
    logger = logging.getLogger(name)
    
    # Avoid adding multiple handlers to the same logger if initialized multiple times
    if logger.hasHandlers():
        logger.handlers.clear()
        
    logger.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # File Handler (rotating log to avoid massive files)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=10485760, backupCount=5  # 10MB per file
    )
    file_handler.setFormatter(formatter)
    
    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
