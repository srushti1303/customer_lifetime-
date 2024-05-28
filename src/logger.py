import logging
import os
from datetime import datetime

# Generate the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the directory path
log_dir = os.path.join(os.getcwd(), "logs")
# log directory exists 
os.makedirs(log_dir, exist_ok=True)

# Create the full log file path
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # messages with severity level
)

if __name__ == "__main__":
    logging.info("Logging has started")
