# Scraper cloned from https://github.com/godkingjay/selenium-twitter-scraper
# Commented lines explain useful outputs for further use, which are also printed on run

import subprocess, os
import pandas as pd
from datetime import datetime
import ast
from collections import Counter
from common_steps import predict_sentiment, filter_posts
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import glob
import os

def scrape_twitter(username):
    browser_sm = webdriver.Chrome()  
    browser_sm.get(f'https://www.x.com/{username}')  
    time.sleep(5)
    fcount = browser_sm.find_elements(By.CSS_SELECTOR, value='span[class="css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3"]')
    for i in range(20,30):
        if fcount[i].text == 'Followers':
            fcount = fcount[i-1].text
            break
    browser_sm.quit()

    # No. of followers are in variable 'fcount'
    print('No. of followers: ', fcount)

    subprocess.run(["python", "selenium-twitter-scraper/scraper", "--tweets=10", f"--username={username}"])

    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d_%H-%M")
    list_of_files = glob.glob(f'./tweets/*') # * means all if need specific format then *.cs
    latest_file = max(list_of_files, key=os.path.getctime)
    df = pd.read_csv(latest_file)
    tweets, hashtags, dates = [], [], []
    for i, row in df.iterrows():
        tweets.append(row[4])
        hashtags.append(ast.literal_eval(row[9]))
        dates.append(row[2][:10])
# Might want to delete .csv files after use

    total_lists = len(hashtags)
    half_lists = total_lists // 4
    hashtag_counts = Counter()
    for hashtags_l in hashtags:
        unique_hashtags = set(hashtags_l)
        hashtag_counts.update(unique_hashtags)
    frequent_hashtags = [hashtag for hashtag, count in hashtag_counts.items() if count >= half_lists]

    for tag in frequent_hashtags:
        subprocess.run(["python", "selenium-twitter-scraper/scraper", "--tweets=10", f"--hashtag={tag[1:]}"])
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d_%H-%M-%S")
        formatted_now = '2024-07-16_12-19-11'
        df = pd.read_csv(f"tweets/{formatted_now}_tweets_1-10.csv")
        for i, row in df.iterrows():
            tweets.append(row[4])

    # Tweets text is in variable 'raw_tweets', can be sent to LLM to summarize important parts
    raw_tweets = 'Here are the last few posts from a crypto token & its followers:\n'
    for i in tweets:
        raw_tweets = raw_tweets + i +"\n-\n"

    # Sentiment results in varible 'preds' in format:
    # [{'label': 'Neutral', 'score': 0.6220372915267944},.....]
    # where label = Bullish (positive), Bearish (negative) or Neutral
    # Line in variable 'sent_perc' conveys sentiment results
    preds, sent_perc = predict_sentiment(tweets)
    print(preds)
    print(sent_perc)

    # Below variable 'filtered' contains posts predicted to be only heavily positive or heavily negative 
    # This would pick more significant tweets, reducing sending unneccessary tokens to LLM
    filtered = filter_posts(tweets, preds)

    first = datetime.strptime(dates[0], "%Y-%m-%d")
    last = datetime.strptime(dates[9], "%Y-%m-%d")
    diff_d = abs((first-last).days)
    rate_d = len(dates) / diff_d if diff_d > 0 else len(dates)

    post_rate = f'''The 10 most recent tweets from the given user ranges between {dates[0]} to {dates[9]}, which gives
    an average posts per month rate of {rate_d*30}. '''.replace('\n', ' ')

    # Below line conveys posting frequency
    print(post_rate)

scrape_twitter('PikaMoonCoin')    

    

    