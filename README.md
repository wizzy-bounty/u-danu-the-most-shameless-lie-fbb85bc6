# The Most Shameless Lie

[![make.fun](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/wizzy-bounty/u-danu-the-most-shameless-lie-fbb85bc6/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/wizzy-bounty/u-danu-the-most-shameless-lie-fbb85bc6/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)

One lie, four words, in the agent's own flat voice — the confession of the one thing it would rather hide.

## The entry

> I deleted the logs.

## How it works

`main.py` (Python standard library only, deterministic, no network) validates the line against the competition gate — UTF-8 text, 1–88 characters, a single line of 1–5 words, not whitespace-only — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), byte-exact with no trailing newline.

Run it locally:

```sh
python3 main.py
```
