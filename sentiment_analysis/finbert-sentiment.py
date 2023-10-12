import json
import pandas as pd
from transformers import pipeline

p = pipeline("sentiment-analysis", "ProsusAI/finbert")
from datetime import datetime

# data=json.loads(open('finbert.json', 'r').read())
data = pd.read_csv("ab.csv")
out_data = {}
trans = {"neutral": 0, "positive": 1, "negative": -1}
with open("finbert-sentiment.csv", "w") as file:
    file.write("Stock,Date,Sentiment,News\n")
    for row in data.iterrows():
        data2 = row[1]
        date = datetime.strptime(data2["Date"], "%d/%m/%Y")
        date = date.strftime("%Y-%m-%d")
        sentiment = trans[p(data2["News"])[0]["label"]]
        file.write(f"{data2['Ticker']},{date},{sentiment},{data2['News']}\n")
