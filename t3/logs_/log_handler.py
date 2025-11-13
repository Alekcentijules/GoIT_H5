from pathlib import Path
from collections import Counter

def parse_log_line(line: str) -> dict:
    """
    Parses a log line into a dictionary.

    Args:
        line (str): Log line.

    Returns:
        Dictionary with keys 'date', 'time', 'level', 'message'.
    """
    line = line.split(" ", 3)
    log = {'data': line[0], 'time': line[1], 'level': line[2], 'info': line[3]}
    return log

def load_logs(file_path: str) -> list:
    """
    Loads logs from a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        logs (list): List of parsed logs.
    """
    logs = []
    with open(Path(file_path), "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                logs.append(parse_log_line(line))
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters logs by level.

    Args:
        logs (list): List of logs.
        level (str): Level (INFO, ERROR, etc.).

    Returns:
        logs (list): Filtered logs.
    """
    return list(filter(lambda log: log['level'] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of logs by level.

    Args:
        logs (list) List of logs.

    Returns:
        dict (str, int): Dictionary {level: count}.
    """
    return Counter(log['level'] for log in logs)

def display_log_counter(counts: dict):
    """
    Displays statistics in table form.

    Args:
        dict (str, int): Dictionary with counts.
    """
    print("Level of log | Quality")
    print("-------------|--------")
    for level, count in counts.items():
        print(f"{level:<12} | {count}")