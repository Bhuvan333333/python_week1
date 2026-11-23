import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calculate_squares():
    numbers = range(1, 21)
    squares = list(map(lambda number: number ** 2, numbers))
    logger.info("Squares calculated successfully")
    return squares

if __name__ == "__main__":
    print(calculate_squares())