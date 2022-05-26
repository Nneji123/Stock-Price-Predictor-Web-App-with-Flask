# Stock Price Predictor Web App 
In this project I developed a machine learning model and a web app with flask for the backend and html, css for the frontend to predict stock prices. 


## Data
The data used was gotten from Yahoo Finance using the yfinance api. To use the api run the following:
```
pip install yfinance
import yfinance as yf
data = yf.download("Name of Stock","Starting date", "Ending Date", auto_adjust = true)
```
- The name of stock I used was USD
- Starting date: 2010-01-01
- Closing date: 2022-04-30

## Algorithm Used
In this project I tested 3 different algorithms namely:
1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. Support Vector Machine
The final model used for the flask app was the linear regression model which had a r2 score of 0.999.


## Requirements
To run a demo do the following:
1. Clone the repository.
2. Install the requirements from the requirements.txt file:
```
pip install -r requirements.txt
```
3. Then from your command line run:
```
python app.py
```
Then you can view the site on your local server: http://127.0.0.1:5000/ 

## Deployment
Yet to be deployed