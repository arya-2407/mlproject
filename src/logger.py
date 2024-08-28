import logging
import os
from datetime import datetime

# Define the log filename with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path to the directory where logs will be stored
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Combine the directory path and log file name to create the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


