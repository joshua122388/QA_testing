def greet(name: str) -> str:
    """
    Return a friendly greeting.
    Examples:
    >>> greet("Josh")
    'Hello, Josh!'
    """
    clean = (name or "").strip()
    return f"Hello, {clean or 'World'}!"


def load_names_from_file(path: str) -> list[str]:
    """
    Load names (one per line) from a text file, skipping blanks.
    """
    names = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if name:
                names.append(name)
    return names
