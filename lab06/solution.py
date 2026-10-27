def count_by_extension(paths: list[str]) -> dict[str, int]:
    
    counts: dict[str, int] = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        base, dot, ext = name.rpartition(".")
        # расширение есть, только если точка не первая в имени
        ext = ext.lower() if dot and base else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths: list[str]) -> str:
    
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))

def human_size(n_bytes: int) -> str:
    
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    if index == 0:
        return f"{int(size)} Б"
    return f"{size:.1f} {units[index]}"