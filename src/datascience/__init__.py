import os
import sys
import logging

# Define the log message format with placeholders for time, level, module, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory where the log file will be saved
log_dir = "logs"

# Full path of the log file (within the log directory)
log_file_path = os.path.join(log_dir, "logging.log")

# Ensure that the log directory exists; create it if it doesn't
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO (captures INFO and more severe messages)
    format=logging_str,  # Set the format for log messages using the previously defined format string
    handlers=[
        # Handler to write log messages to a file
        logging.FileHandler(log_file_path),
        # Handler to print log messages to the standard output (console)
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a named logger instance for the application
logger = logging.getLogger("datasciencelogger")