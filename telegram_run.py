# This code in telescrape.py is taken from another repo -
#  https://github.com/systemadminbdofficials/Telegram-Analysis

import subprocess
import json, os
import pandas as pd
from urllib.request import urlopen
from common_steps import predict_sentiment, filter_posts
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def scrape_telegram(url):
    subprocess.run(["python", "telescrape.py", url])

    name = url.split('/')[-1]
    url = f"https://api.telegram.org/bot{os.environ.get('token1')}:{os.environ.get('token2')}/getChatMemberCount?chat_id=@{name}"
    with urlopen(url) as f:
        followers = json.load(f)['result']

    # No. of followers in variable 'followers'
    print('No. of followers: ', followers)

    with open('channel_messages.json', 'r') as file:
        data = json.load(file)
    raw_posts = 'Here are the last few posts from a crypto token:\n'

    posts, dates = [], []
    for entry in data[:5]:
        dates.append(entry['date'])
        if 'message' in entry.leys():
            posts.append(entry['message'].strip())
            raw_posts = raw_posts + entry['message'].strip()+"\n-\n"
    # Messages text is in variable 'raw_posts', can be sent to LLM to summarize important parts
    print(raw_posts)
    
    # Sentiment results in varible 'preds' in format:
    # [{'label': 'Neutral', 'score': 0.6220372915267944},.....]
    # where label = Bullish (positive), Bearish (negative) or Neutral
    # Line in variable 'sent_perc' conveys sentiment results
    preds, sent_perc = predict_sentiment(posts)
    print(preds)
    print(sent_perc)

    # Below variable 'filtered' contains posts predicted to be only heavily positive or heavily negative 
    # This would pick more significant tweets, reducing sending unneccessary tokens to LLM
    filtered = filter_posts(posts, preds)

    first = datetime.strptime(dates[0], "%Y-%m-%d")
    last = datetime.strptime(dates[9], "%Y-%m-%d")
    diff_d = abs((first-last).days)
    rate_d = len(dates) / diff_d if diff_d > 0 else len(dates)

    post_rate = f'''The 10 most recent messages from the given link ranges between {dates[0]} to {dates[9]}, which gives
    an average messages per month rate of {rate_d*30}. '''.replace('\n', ' ')

    # Below line conveys interaction frequency
    print(post_rate)
    