import os

def delete_data():
    with open('stocks.txt', 'r') as f:
        for ticker in f:
            Symbol= ticker.strip()
            target_file= (f'historical_data\\{Symbol}.csv')
            os.remove(target_file)

delete_data()