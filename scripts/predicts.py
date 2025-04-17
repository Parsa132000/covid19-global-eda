from sklearn.linear_model import LinearRegression
import pandas as pd

def predict_next_7_days(df, country):
    cdf = df[df['location'] == country][['date', 'new_cases']].dropna()
    cdf['days'] = (cdf['date'] - cdf['date'].min()).dt.days
    X, y = cdf[['days']], cdf['new_cases']
    model = LinearRegression().fit(X, y)

    future = pd.DataFrame({'days': range(X['days'].max()+1, X['days'].max()+8)})
    preds = model.predict(future)
    return preds
