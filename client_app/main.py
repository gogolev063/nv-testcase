import random
import string
import sys
from threading import Timer


TEXT_LENGTH = 16                 # length of the generated strings
GET_ENTRIES_COUNT = 10           # the number of requested entries
MIN_MESSAGE_ENTRIES_COUNT = 10   # the minimum number of entries that must be recorded at the same time
MAX_MESSAGE_ENTRIES_COUNT = 100  # the maximum number of entries that must be recorded at the same time
LOG_INTERVAL = 10                # the duration of the interval for logging the number of deleted entries


def generate_string(length: int) -> str:
    """
    Generates a string of a given length using a specific alphabet
    :param length: The length of the generated string
    :return: The generated string of the specified length
    """

    alphabet = string.ascii_letters + string.digits
    return ''.join(random.sample(alphabet, length))


def add_entries(entries: list) -> None:
    """
    Getting a set number of entries from the application server
    :param entries:
    :return:
    """
    pass


def get_entries(count: int) -> dict:
    """
    Requests a specified number of entries from the application server
    :param count: The number of entries to request on the application server
    :return: Dictionary with entries received from the application server
    """
    entries = {}
    return entries


def delete_entries(ids: list) -> None:
    """
    Calls the delete entries with given IDs on the application server
    :param ids: List of IDs to delete
    :return:
    """
    pass


def log(message: str) -> None:
    """
    Writing a specified message to the standard output stream
    :param message: The message that needs to be written to the standard output stream
    :return:
    """
    stdout_file = sys.stdout
    stdout_file.write(message + '\n')


def log_deleted_entries_count() -> None:
    """
    Writing the number of deleted entries to the standard output stream every LOG_INTERVAL seconds
    :return:
    """
    log(str(deleted_count))
    Timer(LOG_INTERVAL, log_deleted_entries_count).start()


deleted_count = 0
log_deleted_entries_count()
while True:
    add_entries([generate_string(TEXT_LENGTH)
                 for i in range(random.randint(MIN_MESSAGE_ENTRIES_COUNT,
                                               MAX_MESSAGE_ENTRIES_COUNT))])
    records = get_entries(GET_ENTRIES_COUNT)
    delete_entries(list(records.keys()))
    deleted_count += len(records)
