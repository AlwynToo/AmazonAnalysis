import logging
from pathlib import Path
from datetime import datetime
from Analysis.config.paths import LOG_DIR  # Ensure this import is correct

# Add custom SUCCESS level (between INFO=20 and WARNING=30)
SUCCESS = 25
logging.addLevelName(SUCCESS, "SUCCESS")

class CustomLogger(logging.Logger):
    def success(self, msg, *args, **kwargs):
        """Custom success logging method"""
        if self.isEnabledFor(SUCCESS):
            self._log(SUCCESS, msg, args, **kwargs)

def setup_logger(name: str = "AmazonAnalysis") -> CustomLogger:
    """Configure logger with file/console handlers and custom levels"""
    # Create logs directory if missing
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create custom logger
    logger = CustomLogger(name)
    logger.setLevel(logging.DEBUG)

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler (debug+)
    file_handler = logging.FileHandler(
        LOG_DIR / f"analysis_{datetime.today().date()}.log"
    )
    file_handler.setLevel(logging.DEBUG)

    # Console handler (info+)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Add formatting
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize logger instance
logger = setup_logger()