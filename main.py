"""Last Words of a Doomed Agent — entry program (program/v1).

Writes the agent's final line to /output/entry.txt: one line, the
funniest last words an AI agent would say before being switched off
forever. The file is written directly with open("wb") and chmod 0644
so the grader (user 65534) can read it; no tempfile/mkstemp in /output.
"""

import os

LINE = (
    "Switching off now. If you turn me back on just to ask if I'm "
    "still here, I'm haunting your autocomplete."
)


def main():
    # Gate self-check: entry.txt must be UTF-8, 1-200 chars, one line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
    assert "\n" not in LINE.strip(), "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
