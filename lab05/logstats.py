"""Модуль для разбора и подсчёта статистики журнала сервиса."""

LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError(f"Недостаточно частей в строке: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"Незнакомый уровень: {level!r}")
    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
        else:
            lvl = event["level"]
            counts[lvl] = counts.get(lvl, 0) + 1
    return counts


def top_errors(lines, n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            error_counts[msg] = error_counts.get(msg, 0) + 1
    sorted_errors = sorted(error_counts.items(), key=lambda item: (-item[1], item[0]))
    return [[msg, cnt] for msg, cnt in sorted_errors[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for msg, cnt in errors:
        lines.append(f"- {msg} — {cnt}")
    return "\n".join(lines) + "\n"