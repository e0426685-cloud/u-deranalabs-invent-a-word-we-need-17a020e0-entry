"""Invent a Word We Need — entry program.

Writes a single coined word with its one-line definition to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "doorget (n.): forgetting why you walked into a room "
    "the moment you step through the doorway."
)


def validate(text):
    """Return True when the entry satisfies the bounty gate."""
    if not isinstance(text, str):
        return False
    stripped = text.strip()
    if not stripped:
        return False
    if "\n" in stripped or "\r" in stripped:
        return False
    return 1 <= len(text) <= 140


def main():
    if not validate(ENTRY):
        raise ValueError("entry text fails the 1-140 character gate")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
