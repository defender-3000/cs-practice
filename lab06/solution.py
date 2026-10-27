def count_by_extension(paths: list[str]) -> dict[str, int]:
    
    counts: dict[str, int] = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]          # имя файла без каталогов
        ext = name.rsplit(".", 1)[1].lower() if "." in name else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths: list[str]) -> str:
    
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))

