Use:  
This repo scrapes posts/messages from various social media sites. It also predicts the sentiment & intensity of sentiment, and posting frequency. Codes taken from many repos, credits given below.   

Instructions:  
First, follow below steps for target site to add credentials & make scraping work.  

Twitter -   
Go to selenium-twitter-scraper folder, and change .env.example file name to .env (just removing example), & add your account creds like below in it.  
TWITTER_USERNAME=xyz123  
TWITTER_PASSWORD=password123  
You can now go ahead & inspect main.py & telegram_run.py to scrape desired accounts, and use their outputs.   

Telegram -  
In main dir, change tel_config.ini.example file name to tel_config.ini (just removing example), & add your account creds like below in it. you can get your api ID & hash by following steps here: https://core.telegram.org/api/obtaining_api_id.   
api_id = 000000000000  
api_hash = kvhefbfk2734874336fbjfvnces5h  
phone = +000000000000  
username = xyz123  
After this, you will have to run telescrape.py, where you will be prompted to enter your number again, and also an OTP that you will recieve on your telegram account. Enter that, and a session will be started, creating some config files in the dir so that  you won't have to manually do this every time you want to scrape. Enter a URL and let it run. You have now setup the telegram scraper, you can go ahead & inspect main.py & telegram_run.py to scrape desired URLs whenever you want, and use their outputs.   

Discord -   
In main dir, and change .env.example file name to .env (just removing example), & add your authentication like below in it. To obtain this value, follow this short video - https://www.youtube.com/watch?v=YEgFvgg7ZPI.   
dis_auth = dcwibevfu234ut5bhj54b6bijnkml  
You can now go ahead & inspect main.py & telegram_run.py to scrape desired servers & channels, and use their outputs. The details required to scrape are the server & channel IDs, not urls or names. You can get those using the app on your phone, in the options under server/channel name (make sure developer mode is on).   


Credits:  
Main scraper files are taken from the below repos.  
Twitter - https://github.com/godkingjay/selenium-twitter-scraper   
Telegram - https://github.com/systemadminbdofficials/Telegram-Analysis   
Discord - https://github.com/lorenz234/Discord-Data-Scraping   
Sentiment Analysis Model - https://huggingface.co/AfterRain007/cryptobertRefined   

