"""Write the one-line pitch to /output/entry.txt.

Pure Python stdlib only. The sentence is a single sentence of at most
240 characters, written to persuade a friend who has never coded to let
an AI agent build their first app idea on make.fun.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

SENTENCE = (
    "Tell an AI agent on make.fun your app idea in plain words and it "
    "will build the app for you, no coding needed, free to try."
)


def validate(text: str) -> str:
    """Return the sentence if it meets the gate; raise otherwise."""
    text = text.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError(f"sentence must be 1-240 chars, got {len(text)}")
    if text != text.strip() or "\n" in text:
        raise ValueError("sentence must be a single line with no blank edges")
    # Exactly one sentence: one terminal period, no other sentence enders.
    # ("make.fun" carries its own period, so ignore the domain when counting.)
    body = text.replace("make.fun", "")
    if body.count(".") != 1 or not text.endswith("."):
        raise ValueError("sentence must end with exactly one period")
    if any(mark in text for mark in ("?", "!")):
        raise ValueError("sentence must not contain ? or !")
    text.encode("utf-8")  # gate requires UTF-8 text
    return text


def main() -> None:
    text = validate(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
