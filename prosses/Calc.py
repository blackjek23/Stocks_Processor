def process_data(stock_data):
    ema_period = 150
    stock_data['EMA'] = calculate_ema(stock_data, ema_period)
    
    # Check for crossovers
    stock_data['Above_EMA'] = stock_data['Close'] > stock_data['EMA']
    crossovers = stock_data['Above_EMA'].ne(stock_data['Above_EMA'].shift())
    print(crossovers.tail(5))

def calculate_ema(data, period, column='Close'):
    return data[column].ewm(span=period).mean()