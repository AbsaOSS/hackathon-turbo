import json
import pandas as pd
from datetime import datetime
from llama_cpp import Llama

llm = Llama(
    model_path="./speechless-llama2-hermes-orca-platypus-wizardlm-13b.Q5_K_S.gguf"
)
data = pd.read_csv("ab.csv")
trans = {"neutral": 0, "positive": 1, "negative": -1}
with open("llama.csv", "w") as file:
    file.write("Stock,Date,Sentiment,News\n")
    for row in data.iterrows():
        data2 = row[1]
        date = datetime.strptime(data2["Date"], "%d/%m/%Y")
        date = date.strftime("%Y-%m-%d")
        #   sentiment = trans[p(data2['News'])[0]['label']]
        prompt = f"Act as a expert trader who from following article needs to decide if he should buy or short stock Absa group (ABG). Include percentage you are certain about that decision. Article follows: {data2['News']}"
        inpt = f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:"""
        output = llm(inpt)
        print(output)
        file.write(f"{data2['Ticker']},{date},{output},{data2['News']}\n")
        file.flush()
