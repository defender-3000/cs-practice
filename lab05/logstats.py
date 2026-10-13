LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    """Разбирает строку журнала в словарь {"time", "level", "message"}.

    Негодная строка (без уровня или с незнакомым уровнем) → ValueError.
    """
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError(f"Недостаточно частей в строке: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"Незнакомый уровень: {level!r}")
    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    """Считает, сколько строк каждого уровня.

    Испорченные строки попадают под ключ BROKEN.
    """
    counts = {level: 0 for level in LEVELS}
    counts["BROKEN"] = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] += 1
        else:
            counts[event["level"]] += 1
    return counts

def top_errors(lines, n: int) -> list[list]:
    """n самых частых сообщений уровня ERROR.

    Пары [сообщение, сколько раз]. При равенстве — по алфавиту.
    """
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

    # сортировка: сначала по убыванию частоты, затем по алфавиту
    sorted_errors = sorted(error_counts.items(), key=lambda item: (-item[1], item[0]))
    return [[msg, cnt] for msg, cnt in sorted_errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    """Формирует текст отчёта по готовым подсчётам."""
    lines = ["Отчёт по журналу"]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("Частые ошибки:")
    for msg, cnt in errors:
        lines.append(f"- {msg} — {cnt}")
    return "\n".join(lines) + "\n"
