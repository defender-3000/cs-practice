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

