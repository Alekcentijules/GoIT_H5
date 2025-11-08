"""The main script for analyzing log files."""
import sys 
from typing import NoReturn
from logs_.log_handler import (load_logs, count_logs_by_level, display_log_counter, filter_logs_by_level)

def main() -> NoReturn:
    """
    Runs log file analysis from command line arguments.

    Usage:
        python main.py <path_to_file> [level]

    Examples:
        python main.py data_/logs.txt
        python main.py data_/logs.txt error
    """
    if len(sys.argv) not in (2, 3):
        print('You need to use: python main.py <path_to_file> [level]')
        return
    file_path = sys.argv[1]
    level = sys.argv[2].upper() if len(sys.argv) == 3 else None

    try:
        logs = load_logs(file_path)
        if not logs:
            print("The file is empty or does not contain valid records.")
            return
        counts = count_logs_by_level(logs)
        display_log_counter(counts)

        if level:
            filtered = filter_logs_by_level(logs, level)
            if filtered:
                print(f"\nLog details for level: {level}")
                for log in filtered:
                    print(f"{log['data']} {log['time']} - {log['info']}")
            else:
                print(f"No level records: {level}")
                
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == '__main__':
    main()