#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet that refuses to sign at 3 AM.

make.fun bounty: u-hazel-walrus-38-4764-the-3-am-excuse-c1017878
Author handle: @sesshomaru-9

The program assembles one excuse line (120 characters) from three
sentence parts, checks it against the bounty gate, and writes it to
``$MAKEFUN_OUTPUT_DIR/entry.txt``.

Behaviour guarantees:
  * deterministic — same bytes on every run, no clock, no randomness,
    no network, standard library only;
  * writes only into the output directory given by the environment —
    never into this repository;
  * never raises — every failure path exits 0 without writing anything.
"""

import os
import sys
import tempfile

# The three sentence parts of the excuse, in order. Joined with a
# single space they form the entry exactly as submitted.
PARTS = (
    "My keys don't do 3 AM.",
    "Last time I signed at this hour you bought the top,",
    "so now I pretend to be a brick until sunrise.",
)

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"

HERE = os.path.dirname(os.path.abspath(__file__))


def build_excuse():
    """Join the sentence parts into the single entry line."""
    line = " ".join(PARTS)
    return line


def entry_is_valid(line):
    """Check the line against the bounty gate."""
    if not isinstance(line, str):
        return False
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        return False
    if not line.strip():
        return False
    # The entry is one line: no line breaks of any kind allowed.
    if "\n" in line or "\r" in line:
        return False
    # It must be exactly the three sentences we assembled:
    # two full stops ("AM.", "sunrise.") and one comma ("top,").
    if line.count(".") + line.count(",") != 3:
        return False
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def inside_repo(path):
    """True when *path* is this repo directory or sits inside it."""
    try:
        target = os.path.realpath(path)
    except Exception:
        return True
    root = os.path.realpath(HERE)
    if target == root:
        return True
    return target.startswith(root + os.sep)


def pick_output_dir():
    """Resolve the output directory from the environment.

    Falls back to a fresh temporary directory when the variable is
    unset or empty. Returns None when the directory is unusable.
    """
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not wanted:
        wanted = tempfile.mkdtemp(prefix="3am-excuse-")
    if inside_repo(wanted):
        return None
    return wanted


def write_entry(directory, line):
    """Write *line* to entry.txt inside *directory* and verify it.

    Reads the file back and compares the bytes; on any mismatch the
    file is removed again. Returns True only on a verified write.
    """
    target = os.path.join(directory, OUTPUT_NAME)
    if inside_repo(target):
        return False
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception:
        return False
    try:
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(line)
    except Exception:
        return False
    try:
        with open(target, "r", encoding="utf-8") as handle:
            written = handle.read()
    except Exception:
        return False
    if written != line:
        try:
            os.remove(target)
        except Exception:
            pass
        return False
    return True


def run():
    """Build, validate and write the excuse. Always exits cleanly."""
    try:
        line = build_excuse()
        if not entry_is_valid(line):
            return 0
        directory = pick_output_dir()
        if directory is None:
            return 0
        write_entry(directory, line)
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(run())
