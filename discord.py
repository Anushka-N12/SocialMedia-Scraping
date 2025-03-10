"""
Created on Mon Sep 20 11:01:50 2021
@author: Lorenz234
https://github.com/lorenz234/Discord-Data-Scraping
"""

# Examples for scraping data from discord servers (a.k.a. guilds) 
# (see README.md on how to find out the server_id and channel_id)

# import libraries to make get request
import requests, json, os
from dotenv import load_dotenv
load_dotenv()

# your API Key goes here (see README.md on how to find out your own api key)
h = {
    "authorization": os.environ.get('dis_auth')
 }

# approximate_member_count (count of server members)
def get_approximate_member_count(server_id):
    r = requests.get('https://discord.com/api/guilds/' + str(server_id) + '/preview', headers=h)
    j = json.loads(r.text)
    return j['approximate_member_count']

# approximate_presence_count (count of currently online server members)
def get_approximate_presence_count(server_id):
    r = requests.get('https://discord.com/api/guilds/' + str(server_id) + '/preview', headers=h)
    j = json.loads(r.text)
    return j['approximate_presence_count']

# get the text content of the last 10 messages postet to a specific channel/direct message
def get_last_20_messages_from_channel(channel_id):
    r = requests.get('https://discord.com/api/v9/channels/' + channel_id + '/messages?limit=20', headers=h)
    j = json.loads(r.text)
    m = [c['content'] for c in j]
    return m

        