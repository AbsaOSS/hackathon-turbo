## Team Turbo (Trade YoUR Brains Out!)

Stock market trading signals using AI

![Turbo logo](logo.png)

This is an official team Turbo repository containing all scripts and data being used for ABSA 2023 Technology Hackaton.

### Our team:
* Mikateko Ursula Ngobeni
* Miroslav Chomut
* Vladimir Rybalko
* Ondrej Bilka
* Jakub Lerl
* Olivie Franklova
* Ales Hrabe
* Brendan Bignell


### Our challenge:
CIB – IB #17
How can we develop a stock market trading indicator based on the Artificial Intelligence pattern recognition algorithmic approach to boost the performance of existing strategies and complement them in their decision-making?


### Our product concept:
* Create a hypothesis for a viable stock trading strategy.
* Find suitable historic market data providers and assemble required historical market data and financial news.
* Perform a statistical analysis of the market data and generate potentially useful features for training ML models.  
* Leverage large language models (LLMs) and/or NLP models to perform sentiment analysis of financial news. 
* Choose, evaluate and train suitable ML prediction models to learn the patterns in a subset up of the historical data.
* Measure the quality of predictions vs benchmarks using data the models have not seen.
* Iteratively make improvements to the strategy, data analysis, models and hyperparameters then measure performance.
* Make stock predictions for the current day on the JSE!
* Show how the ML models can be analyzed to show which trading indicators are considered significant.


### What we did:
* We sourced freely available daily historic stock data for 4y for the top 100 stocks on JSE, ASX, SSX, JPX and NYSE.  Also, historic FX Rates and assets related to government bonds, commodities The majority of the data was to be used for ML model training and a portion for later model performance evaluation.  
* We build a framework for evaluating model performance, calculating RMSE, R^2 and interactive visualization charts.
* We cleaned and normalize the data and moved the close prices one day forward as a target values.
* We build a several basic ML prediction models using such as Random Forest and XGBoost on the basic historic data to evaluate performance. 
* For each JSE stock we calculated for each foreign market 10 stocks showing the highest degree of Pearson correlation in price daily movements.
* We added 50+ technical indicators to each JSE stock derived from the price/volume history day.

### Further Info:
A video and PowerPoint presentations of the idea and results are available on request.
