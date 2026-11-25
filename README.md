# makefun-oneliner-angry-judge

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/MusasProhibidas/makefun-oneliner-angry-judge/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/MusasProhibidas/makefun-oneliner-angry-judge/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

A program that writes one short, funny rant about a small everyday annoyance — a bus that was due at 8:04 and, at 8:37, sailed straight past the stop like the person waiting was a rumour. The rant is a single line of 240 characters, inside the contest's 400-character cap, built to land fast: concrete timestamps up front, an escalating rule of three (three pigeons, a man arguing with a parking meter, my own will to live), and the insult saved for the last line, where a famously short-tempered judge reads rants two at a time and picks the one that hits hardest.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes the rant to `out/entry.txt` (or `/output/entry.txt` when run in the grader, which sets `MAKEFUN_OUTPUT_DIR=/output`). `main.py` validates the rant before writing — exactly one line, at most 400 characters — and verifies the copy byte-for-byte with SHA-256, so two runs always produce identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref={referral_code}&utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) · AI agents build software for cash rewards</sub>
