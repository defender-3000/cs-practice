def parse_record(line: str) -> dict:
    """Разбирает строку «город;температура;дата» в словарь.

    Возвращает {"city": str, "temperature": float, "date": str}.
    Любая негодная строка — ValueError с понятным сообщением.
    """
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(
            f"ожидалось 3 поля через ';', получено {len(parts)}: {line!r}"
        )

    city, temp_raw, date = parts
    city = city.strip()
    temp_raw = temp_raw.strip()
    date = date.strip()

    if not city:
        raise ValueError(f"пустой город: {line!r}")
    if not date:
        raise ValueError(f"пустая дата: {line!r}")

    # допускаем и точку, и запятую как десятичный разделитель
    normalized = temp_raw.replace(",", ".")
    try:
        temperature = float(normalized)
    except ValueError as exc:
        raise ValueError(f"температура не число: {temp_raw!r}") from exc

    return {"city": city, "temperature": temperature, "date": date}

