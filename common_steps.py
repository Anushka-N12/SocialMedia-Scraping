# Model taken from https://huggingface.co/AfterRain007/cryptobertRefined 

from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer

def predict_sentiment(posts):
    model_name = "AfterRain007/cryptobertRefined"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels = 3)
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=128, truncation=True, padding = 'max_length')
    preds = pipe(posts)
    bearish_count = sum(1 for item in preds if item['label'] == 'Bearish')
    bullish_count = sum(1 for item in preds if item['label'] == 'Bullish')
    sent_perc = f'''Out of the posts collected, our sentiment analysis model found {int(bullish_count/len(posts)*100)}% 
    of the posts to be positive, and {int(bearish_count/len(posts)*100)}% negative. '''.replace('\n', ' ')
    return preds, sent_perc

def filter_posts(posts, preds):
    filtered = []
    for i in range (len(preds)):
        if preds[i]['score'] > 0.7 and preds[i]['label'] in ['Bearish', 'Bullish']:
            filtered.append(posts[i])
    return filtered