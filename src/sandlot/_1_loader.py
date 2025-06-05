from pathlib import Path


def load(filename: str) -> str:
    """
    Load text file as a string.
    """
    text_file = Path(__file__).resolve().parent / filename

    return text_file.read_text()
