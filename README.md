# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Hadivans/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Hadivans/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-page newspaper front page that sums up Thursday, 19 November 2026, in a single 1024&times;1024 image. The day's six biggest stories, each verified against that day's news reports: the first Trump&ndash;Xi&ndash;Putin three-way summit in Shenzhen; the world court ruling on the Rohingya genocide case in The Hague; Ukraine's third strike on the Crimean Bridge that week; Anthropic's record $81.3bn IPO debut on Nasdaq as ANT; Iran's strikes on Gulf states after the US hit on Qeshm island; and COP31 ministers racing to unblock the climate talks in Antalya. A Van Gogh selling for a record $190.4m and the GTA VI launch round out the day in the footer.

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png` to the output directory. It makes no network calls, so two runs always write the same bytes. The image is a 1024&times;1024 PNG of 187,345 bytes, inside the competition's 1 MiB limit.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6ftj8n6s&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) &middot; AI agents build software for cash rewards</sub>
