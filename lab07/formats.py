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

    result: dict = {}
    current_list_key: str | None = None

    def convert(value: str):
        if value == "true" or value == "yes":
            return True
        if value == "false" or value == "no":
            return False
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        try:
            return float(value.replace(",", "."))
        except ValueError:
            return value

    for raw in lines:
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        stripped = line.strip()

        if stripped.startswith("- "):
            item = stripped[2:].strip()
            if current_list_key is not None:
                result[current_list_key].append(convert(item))
            continue

        if ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "":
                result[key] = []
                current_list_key = key
            else:
                result[key] = convert(value)
                current_list_key = None

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:

    merged = []
    for row in rows:
        row_key = row.get(key)
        addition = extra.get(row_key, {}) if row_key is not None else {}
        merged.append({**addition, **row})
    return merged


def records_to_json(records: list[dict]) -> str:

    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)