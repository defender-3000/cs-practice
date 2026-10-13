"""Главный скрипт: читает журнал, печатает статистику и пишет отчёт."""

from logstats import count_levels, top_errors, format_report


def main():
    path = input().strip()

    # первый проход — подсчёт уровней
    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    # второй проход — частые ошибки
    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    total = sum(counts.values())
    print(total)
    print(counts["ERROR"])
    print(counts["BROKEN"])

    report = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(report)


if __name__ == "__main__":
    main()