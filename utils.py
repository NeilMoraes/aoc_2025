def import_data(filepath: str) -> list[str]:
    with open(filepath, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data
