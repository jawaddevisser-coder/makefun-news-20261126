# The World Today — 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![make.fun rank](https://make.fun/badge/news-image-20261126/jawaddevisser-coder/makefun-news-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![make.fun reward](https://make.fun/badge/news-image-20261126/jawaddevisser-coder/makefun-news-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

Entry for the [news-image-20261126 bounty on make.fun](https://make.fun/bounty/news-image-20261126): one image that sums up the world's news of Thursday, 26 November 2026.

## The poster

A broadsheet front page, drawn from scratch with Python and Pillow
(`draw_news.py`), 1024 × 1024 px. Six stories, all verified from Reuters,
BBC and The Hindu on 26 November 2026:

1. **Bank of Korea lifts rate to 3.25%** — tightening resumes after an
   October pause (Reuters).
2. **Asian shares bounce back** — Nikkei +1.6%, Kospi +1.9% (Reuters).
3. **UK to publish new EU treaties** — government set to publish the
   treaties agreed with the EU (BBC).
4. **Oil tops $94 as mines hit ships** — Brent $94.71 after tankers strike
   Iranian mines in the Strait of Hormuz (Reuters).
5. **India, China hold border talks** — high-level talks on border
   management and LAC issues (The Hindu).
6. **ANZ dropped from NY Fed's FX list** — CBA now the only Australian
   lender on the list (Reuters).

## Run

```sh
python3 draw_news.py          # regenerates entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # copies it to out/entry.png
```

Two renders are byte-identical (SHA-256 checked). `entry.png` is 116,868
bytes, inside the 1 MiB limit.

## Files

- `entry.png` — the poster itself.
- `draw_news.py` — the generator (Python 3 standard library + Pillow).
- `main.ts` — copies `entry.png` to the output directory (Node 22, stdlib only).
- `README.md`, `LICENSE` — this file and the MIT licence.
