import feedparser
import json
import requests
import os


def set_keywords():
    return ['Stock Alert (US): RPi 4 Model B - 4GB RAM',
            'Stock Alert (US): RPi 4 Model B - 8GB RAM']


def post_message_to_slack(blocks=None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': 'SLACK_TOKEN',
        'channel': '#rpilocator',
        'icon_emoji': ':pie:',
        'username': 'rpilocator',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()


def get_existing_published_dates():
    viewed_items = open(script_directory + '/viewed_items.txt', 'r')
    existing_dates = viewed_items.readlines()
    existing_dates = [date.rstrip() for date in existing_dates]
    viewed_items.close()
    return existing_dates


def published_date_is_new(date):
    if date in existing_published_dates:
        return False
    else:
        return True


def contains_match(title):
    for word in keywords:
        if word.lower() in title:
            return True
    return False


def process_feed(feed):
    for key in feed["entries"]:
        title = key['title']
        link = key['link']
        published_date = key['published']

        if published_date_is_new(published_date) and contains_match(title.lower()):
            print('{} - {}'.format(title, published_date))

            blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*" + title + "*\n\n<" + link + "|View on rpilocator>"
                    }
                }
            ]
            json.loads(json.dumps(post_message_to_slack(blocks)))

            with open(script_directory + '/viewed_items.txt', 'a') as f:
                f.write('{}\n'.format(published_date))


keywords = set_keywords()
script_directory = os.path.dirname(__file__)
existing_published_dates = get_existing_published_dates()
process_feed(feedparser.parse('https://rpilocator.com/feed.rss'))
