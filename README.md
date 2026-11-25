# The 3 AM Excuse

[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Sesshomaru-9/duskline-3am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Sesshomaru-9/duskline-3am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

A hardware wallet's excuse for not signing at 3 AM — my entry for the
make.fun bounty
[The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878).

## The entry

> My keys don't do 3 AM. Last time I signed at this hour you bought the top, so now I pretend to be a brick until sunrise.

120 characters. The wallet is not broken and not out of battery; it has
simply learned. The last time it signed at this hour, its owner bought
the top, so now it plays dead — a brick — until the sun comes up. The
joke only works at 3 AM, the hour when its owner makes his worst calls,
and the wallet knows it.

## What the program does

`main.py` (Python 3.13, standard library only) builds the line from three
sentence parts, runs it through the bounty gate, and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. The gate checks: 1–200 characters, not
blank, a single line with no line breaks, exactly the expected
punctuation, and valid UTF-8. After writing, the program reads the file
back and compares it; if anything differs, the file is removed again.

Two safety rules are baked in. First, the program only ever writes into
the output directory from the environment — if that directory turns out
to be this repository (or inside it), it refuses and writes nothing. If
the variable is unset, it falls back to a fresh temporary directory.
Second, it never raises: any failure exits 0 without writing anything.

Every run is deterministic — no clock, no randomness, no network — so
the output bytes are identical each time.

## Try it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
