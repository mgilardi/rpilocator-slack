# Raspberry Pi Locator for Slack

The goal of this script is to filter the [rpilocator RSS feed](https://rpilocator.com/feed.rss) data down by desired Pi type(s) and then sending a Slack message when there's availability.

1. Create a Slack bot and use the specified token in the config
2. Set desired Pi types as keywords (matching the title on rpilocator.com)
3. Run this (or a variation of it) with crontab (crontab -e):

```
* * * * * /usr/local/bin/python3 /path/to/rpilocator-slack/rpilocator-slack.py
```

**The rpilocator tool was created by André Costa of DPHacks.com and rpilocator.com. Thanks, André!**
