import json
import logging
from pathlib import Path

import mysql.connector
from mysql.connector import Error

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "config.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def load_config():
    try:
        with open(CONFIG_PATH, encoding="utf-8") as file:
            return json.load(file)["mysql"]

    except (OSError, json.JSONDecodeError) as error:
        logger.exception("Unable to load configuration")
        raise RuntimeError("Configuration loading failed") from error


def get_connection():
    config = load_config()
    try:
        connection = mysql.connector.connect(**config)
        logger.info("MySQL connection established")
        return connection

    except Error:
        logger.exception("Database connection failed")
        raise


def fetch_employees(batch_size=1000):
    """Fetch employee records using a generator.Only one batch is fetched at a time."""
    connection = None
    cursor = None

    try:
        connection = get_connection()

        cursor = connection.cursor(dictionary=True,buffered=False)

        cursor.execute("SELECT emp_no, first_name, last_name FROM employees")

        while True:
            records = cursor.fetchmany(batch_size)

            if not records:
                break

            for record in records:
                yield record

        logger.info("Employee fetching completed")

    except Error:
        logger.exception("Error while fetching employees")
        raise

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
            logger.info("Database connection closed")


def process_employees():
    """Process employee records one at a time."""
    count = 0

    for employee in fetch_employees():
        count += 1

        logger.debug("Processing employee: %s", employee["emp_no"])

    logger.info("Total employees processed: %d", count)


if __name__ == "__main__":
    process_employees()