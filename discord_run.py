"""
Main scraping code in discord.py taken from below repo
https://github.com/lorenz234/Discord-Data-Scraping
@author: Lorenz234
"""

from discord import get_approximate_member_count, get_last_20_messages_from_channel
from common_steps import predict_sentiment, filter_posts

def scrape_server(s_id, c_id_l):

    # No. of followers in variable 'followers'
    followers = get_approximate_member_count(s_id)
    print('No. of followers: ', followers)

    raw_msgs = 'Here are the last few messages from a crypto token\'s discord:\n'
    messages = []       # Dates weren't available in this scraper
    for c_id in c_id_l:
        c_msgs = get_last_20_messages_from_channel(c_id)
        for msg in c_msgs:        
            messages.append(msg)
            raw_msgs = raw_msgs + msg +"\n-\n"

    # Messages text is in variable 'raw_msgs', can be sent to LLM to summarize important parts
    print(raw_msgs)
    
    # Sentiment results in varible 'preds' in format:
    # [{'label': 'Neutral', 'score': 0.6220372915267944},.....]
    # where label = Bullish (positive), Bearish (negative) or Neutral
    # Line in variable 'sent_perc' conveys sentiment results
    preds, sent_perc = predict_sentiment(messages)
    print(preds)
    print(sent_perc)

    # Below variable 'filtered' contains posts predicted to be only heavily positive or heavily negative 
    # This would pick more significant tweets, reducing sending unneccessary tokens to LLM
    filtered = filter_posts(messages, preds)

scrape_server('1262577757930524756', ['1262810376777760768'])