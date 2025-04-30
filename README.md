## Refer to our report for a full description of what each file does
## DS 340 Final Project by Emir Tali and Sam Cowan

### Introduction:

Predicting the stock market is hard. It’s a trillion dollar question that everyone would like to solve. In this paper, we flip this question on its head: is it possible to predict the stock market if you have access to future information? This is not just a question of time travel, but it also pertains to the persistence of insider trading, using information not public yet to unfairly trade in the market. Notoriously, many Congressmen engage in this activity. However, is it possible to _reliably_ use future news to make money today? 

Our starting point was based on Haghani et al’s “When a Crystal Ball Isn’t Enough to Make You Rich”, an experiment in which 118 finance majors were challenged to make money in the stock and bond markets given a redacted version of the next day’s front page of the Wall Street Journal. These players did not do very well, barely averaging 50% correct on the direction of the stock movement. However, 5 experienced traders who completed the same challenge gained 130% profit on average (after 15 rounds of betting). So to the untrained eye, it looks like all one can do is just blindly guess if the stock market will go up or down. However, the experienced traders seem to have an implicit understanding of how news events correlate with stock performance. We sought out to see if a neural network could also learn this understanding by training on news from the next day combined with stocks from the prior day. Our goal was to train a neural network to do better than blind guessing by any amount. 

### Methodology:
Our data was obtained from the front page of the New York Times from 2013 to 2023. We converted the PDFs to text via Pytesseract OCR, and then used the Ollama Nomic embeddings model to get the embeddings for each day through a 24 hour-long SCC batch job. We also obtained stock market data in that time frame from AlphaVantage. Later, when we realized that we needed more data, we identified individual articles from the front pages containing information about finance and business. After separating them, we calculated the embeddings for the individual articles.

We used a deep neural network with dense and dropout layers. All in all, we had three primary datasets: embeddings on full pages, embeddings on articles, and cosine similarity/MLNI (to be explained below). For each dataset, we created a preliminary neural network for regression, a network for classification, ran a hyperparameter tuning session for classification, and a session for regression. This can be seen in ‘neuralnetwork.ipynb.’ Each hyperparameter tuning session ran over 90 trials and we looked at the top 15 to draw our conclusions. 


### How to run our code (if desired):  
- Run `stockdata.py` and then `data_utils.py` after acquiring an AlphaVantage API key  
- Acquire embeddings by going through `Embeddings.ipynb` (you will likely have to edit some things to make it work outside of Colab)  
- Run neural network code in `Neuralnetwork.ipynb`, using the CSVs generated in the prior two steps  
