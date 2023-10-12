Experiments with sentiment analysis.

Baseline we tried is to get historical news for JSE stocks and do sentiment analysis using pretrained
finbert model(file finbert-sentiment.py) however we didn't find a free source of such news.

That approach is widely used in industry, so we aimed to use large language models to find correlations
beyond looking at news about company.
For example model could connect news 'largest copper mine in south africa flooded' with company description
'CPTP is the largest producer of copper pots in south africa' to deduce that CPTP stock will fall.

To do that properly we need to use embedding technique for all news and vector search to find news close to 
company description then use a large language model. For hackaton purposes we used bing chat as closest of the shelf solutions with queries like:

For September 2023 summarize news related to company absa group (ABG) with a timeline containing the date and 4 paragraphs of text for each date, but do not try to balance the sentiment and provide as much verbatim text from reputable news sources as possible.

For September 2023 summarize news related to south african real estate with a timeline containing the date and 4 paragraphs of text for each date, but do not try to balance the sentiment and provide as much verbatim text from reputable news sources as possible.

We were limited to news summarizing due to content filters as asking for sentiment analysis bot replied with phrase that as AI he can't predict future stock prices.

We included example ab.csv of summary of news about absa group in this repository. Trying to use finbert on such summaries didn't work well as they are different from news headlines finbert was trained for.

So we used an open source llama model to do sentiment analysis and it was mostly correct with his predictions(see llama.csv).

Response is free form text which requires further parsing, attempts to give it fixed form decreased performance as model gets more compute time with each word processed it is best to first ask for rationale ending with model suggestion.

To run code on linux machine(use wsl2 for windows) here you first need to create python venv with

python -m venv venv
. venv/bin/activate

Then run install script 
./install.sh

