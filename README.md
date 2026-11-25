# Duskline 3AM Excuse

[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Sesshomaru-9/duskline-3am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Sesshomaru-9/duskline-3am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

One line, in the voice of a hardware wallet that refuses to sign at 3 AM —
entry for the make.fun bounty
[The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878).

## The entry

> My keys don't do 3 AM. Last time I signed at this hour you bought the top, so now I pretend to be a brick until sunrise.

120 characters. One self-contained line: the wallet has a grudge, not a
glitch — it remembers the last 3 AM signature (buying the top) and now
plays dead, a brick, until sunrise. No batteries, no firmware update, no
cold-storage cliché; the 3 AM hour itself is the joke, because the excuse
only makes sense at a time when its owner makes his worst decisions.

## How the program works

`main.py` (Python 3.13, standard library only, deterministic, no network)
holds the line as a constant, validates it against the gate (1–200 characters,
valid UTF-8, not only whitespace), then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and reads it back to confirm the bytes match.

Safety guard: if the resolved output directory is the repository directory
(or inside it), the program refuses to write anything and exits 0. If
`$MAKEFUN_OUTPUT_DIR` is unset it falls back to a fresh temporary directory.
The program never raises: any failure exits 0 without writing.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
