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
