import pandas as pd

def detect_ema_cross(stock_data):
    # Calculate the 150 EMA
    stock_data['150ema'] = stock_data['Close'].ewm(span=150, adjust=False).mean()

    # Detect cross up and cross down
    stock_data['previous_close'] = stock_data['Close'].shift(1)
    stock_data['previous_ema'] = stock_data['150ema'].shift(1)

    # Cross Up: Previous price was below EMA, current price is above EMA
    stock_data['cross_up'] = (stock_data['previous_close'] < stock_data['previous_ema']) & (stock_data['Close'] > stock_data['150ema'])

    # Cross Down: Previous price was above EMA, current price is below EMA
    stock_data['cross_down'] = (stock_data['previous_close'] > stock_data['previous_ema']) & (stock_data['Close'] < stock_data['150ema'])

    # Filter rows where either cross up or cross down occurs
    cross_events = stock_data[(stock_data['cross_up']) | (stock_data['cross_down'])]

    # Drop the columns used for calculation to return only the relevant information
    cross_events = cross_events[['Close', '150ema', 'cross_up', 'cross_down']]
    last_closing_price = stock_data['Close'].iloc[-1]

    print(cross_events.tail(1), '\n' ,last_closing_price)
