import logging
import os
from datetime import datetime

# 1. Define the log file's name

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path for the logs DIRECTORY
# This path points to the folder that will contain your log files.

logs_dir = os.path.join(os.getcwd(), "logs")

# 3. Create the logs directory if it's not already there

os.makedirs(logs_dir, exist_ok=True)

# 4. Create the full, correct FILE path by joining the directory and the filename

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 5. Configure logging using the correct file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has been successfully configured and started.")