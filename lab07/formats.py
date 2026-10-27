import json

def csv_to_records(text: str) -> list[dict]:
    
    if not text.strip():
        return []
    lines = text.splitlines()
    header = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        records.append(dict(zip(header, values)))
    return records

def parse_settings(lines: list[str]) -> dict:
    """Простой YAML: «ключ: значение», списки через «- », комментарии после #."""
    result: dict = {}
    current_list_key: str | None = None

    for raw in lines:
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        stripped = line.strip()

        if stripped.startswith("- "):
            item = stripped[2:].strip()
            if current_list_key is not None:
                # приведение типа элемента списка
                if item == "true" or item == "yes":
                    result[current_list_key].append(True)
                elif item == "false" or item == "no":
                    result[current_list_key].append(False)
                else:
                    try:
                        result[current_list_key].append(int(item))
                    except ValueError:
                        try:
                            result[current_list_key].append(float(item))
                        except ValueError:
                            result[current_list_key].append(item)
            continue

        if ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "":
                result[key] = []
                current_list_key = key
                continue
            # приведение типа обычного значения
            if value == "true" or value == "yes":
                result[key] = True
            elif value == "false" or value == "no":
                result[key] = False
            else:
                try:
                    result[key] = int(value)
                except ValueError:
                    try:
                        result[key] = float(value)
                    except ValueError:
                        result[key] = value
            current_list_key = None

    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из справочника по значению ключа key.

    Поля самой записи важнее: при совпадении ключей остаётся значение из записи.
    """
    merged = []
    for row in rows:
        row_key = row.get(key)
        addition = extra.get(row_key, {}) if row_key is not None else {}
        merged.append({**addition, **row})
    return merged

