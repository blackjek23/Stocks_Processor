import pandas as pd

def detect_ema_cross(df):
    # Calculate the 150 EMA (if not already in the CSV)
    df['150_EMA'] = df['Close'].ewm(span=150, adjust=False).mean()

    # Calculate when the close price crosses above or below the 150 EMA
    df['Cross_Up'] = (df['Close'].shift(1) < df['150_EMA'].shift(1)) & (df['Close'] > df['150_EMA'])
    df['Cross_Down'] = (df['Close'].shift(1) > df['150_EMA'].shift(1)) & (df['Close'] < df['150_EMA'])

    # Send Alerts
    if df['Cross_Up'].iloc[-1]:
        print(df.iloc[-1])

    if df['Cross_Down'].iloc[-1]:
        print(df.iloc[-1])