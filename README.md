# Stock Portfolio Optimization Using Machine Learning

This project builds a machine learning-driven portfolio optimization framework that predicts stock price movements and allocates capital accordingly. It combines predictive modeling, financial feature engineering, and Markowitz optimization to construct a portfolio designed to outperform a passive benchmark.

---

## Objective

- Predict whether each stock will increase in price the next day using logistic regression and technical indicators.
- Use these predictions to construct an optimized portfolio that balances expected return and risk.
- Compare the performance of the optimized portfolio against a simple equal-weight strategy.

---

## Tools & Libraries

- **Data**: Yahoo Finance (`yfinance`)
- **Feature Engineering**: `pandas_ta`
- **Machine Learning**: `scikit-learn`
- **Optimization**: `cvxpy`
- **Visualization**: `matplotlib`, `pandas`

---

## Workflow

### 1. **Data Collection**
Pulled 5 years of daily stock data for five major tech stocks (AAPL, AMZN, GOOGL, META, MSFT) from Yahoo Finance.

### 2. **Feature Engineering**
Computed key technical indicators from the `Close` price:
- Simple Moving Averages (10, 30 days)
- Relative Strength Index (RSI)
- MACD
- Rate of Change (ROC)

### 3. **Target Variable**
Created a binary target:
- `1` if the stock’s price increased the following day
- `0` otherwise

### 4. **Machine Learning Model**
Trained separate **logistic regression** models for each stock using the engineered features to predict the target variable.

### 5. **Portfolio Optimization**
Used the predicted probabilities as expected returns. Solved a mean-variance optimization problem to allocate weights across assets:
- Maximize expected return – λ × portfolio variance
- Subject to constraints: weights sum to 1, no short selling (w ≥ 0), optional max cap per stock

### 6. **Backtesting**
Simulated performance of:
- Optimized portfolio (based on ML predictions)
- Equal-weight portfolio (baseline benchmark)

---

## Results

- **Optimized portfolio** allocated 100% to the stock with the highest expected return under strict constraints.
- After adding diversification constraints, the portfolio balanced across top-performing stocks.
- Backtested returns show relative performance between optimized and equal-weight portfolios (see plot below).

## Next Steps

- Use XGBoost or LightGBM instead of Logistic Regression
- Introduce transaction cost and slippage simulation
- Rebalance portfolio monthly using rolling predictions
- Incorporate macroeconomic indicators or earnings surprises

---

## Author

**Jonathan Adamson**   
📧 [jonathan.adamson324@gmail.com]
🔗 [LinkedIn Profile](https://www.linkedin.com/in/jonathanmadamson/) 

---

## Disclaimer

This project is for educational purposes only and does not constitute financial advice or investment recommendation.

