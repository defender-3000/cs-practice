"""Программа: читает журнал, вызывает функции из stats.py, печатает отчёт."""

import sys

from stats import average_by_city, read_valid, warmest_city

def main() -> None:
    lines = sys.stdin.read().splitlines()

    non_empty = [line for line in lines if line.strip()]
    records = read_valid(lines)

    parsed = len(records)
    skipped = len(non_empty) - parsed

    print(parsed)
    print(skipped)

    if records:
        warm = warmest_city(records)
        avg = average_by_city(records)[warm]
        print(f"{avg:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()