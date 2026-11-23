import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def remove_duplicates(values):
    try:
        unique_values = list(dict.fromkeys(values))
        logger.info("Duplicates removed successfully")
        return unique_values
    except TypeError as error:
        logger.exception("Input contains unhashable values")
        raise ValueError("All elements must be hashable") from error


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 1, 5, 3]

    result = remove_duplicates(numbers)

    print(result)